# Built-ins
import base64
import decimal
import logging
import struct
import zlib
from typing import Iterator, List, Union

# Project
from pobapi.constants import TREE_OFFSET

# Third-party
import requests

logger = logging.getLogger(__name__)


def _fetch_xml_from_url(url: str, timeout: float) -> bytes:
    """Get a Path Of Building import code shared with pastebin.com.

    :raises: :class:`~requests.URLRequired`, :class:`~requests.Timeout`,
        :class:`~requests.ConnectionError`, :class:`~requests.HTTPError`,
        :class:`~requests.TooManyRedirects`, :class:`~requests.RequestException`

    :return: Decompressed XML build document."""
    if url.startswith("https://pastebin.com/"):
        raw = url.replace("https://pastebin.com/", "https://pastebin.com/raw/")
        try:
            request = requests.get(raw, timeout=timeout)
            request.raise_for_status()
        except requests.URLRequired:
            logger.exception(f"{url} is not a valid URL.")
        except requests.Timeout:
            logger.exception(
                f"Connection timed out, try again or raise the timeout ({timeout}s)."
            )
        except requests.ConnectionError:
            logger.exception(
                f"There was a network problem (DNS failure, refused connection, etc)."
            )
        except requests.HTTPError:
            logger.exception(f"HTTP request returned unsuccessful status code.")
        except requests.TooManyRedirects:
            logger.exception(f"Request exceeds the maximum number of redirects.")
        except requests.RequestException:
            logger.exception(f"Some other unspecified fatal error; cannot continue.")
        else:
            return _fetch_xml_from_import_code(request.text)
    else:
        logger.exception(f"{url} is not a valid pastebin.com URL.")


def _fetch_xml_from_import_code(import_code: str) -> bytes:
    """Decodes and unzips a Path Of Building import code.

    :raises: :class:`TypeError`, :class:`ValueError`

    :return: Decompressed XML build document."""
    try:
        base64_decode = base64.urlsafe_b64decode(import_code)
        decompressed_xml = zlib.decompress(base64_decode)
    except (TypeError, ValueError):
        logger.exception("Error while decoding.")
    except zlib.error:
        logger.exception("Error while decompressing.")
    else:
        return decompressed_xml


def _skill_tree_nodes(url: str) -> List[int]:
    """Get a list of passive tree node IDs.

    :return: Passive tree node IDs."""
    *_, url = url.rpartition("/")
    bin_tree = base64.urlsafe_b64decode(url)
    return list(
        struct.unpack_from(
            "!" + "H" * ((len(bin_tree) - TREE_OFFSET) // 2),
            bin_tree,
            offset=TREE_OFFSET,
        )
    )


def _get_stat(text: List[str], stat: str) -> Union[str, type(True)]:
    """Get the value of an item affix.
    If an affix is found without a value, returns True instead.

    :return: Item affix value or True."""
    for line in text:
        if line.startswith(stat):
            *_, result = line.partition(stat)
            return result or True


def _get_pos(text: List[str], stat: str) -> int:
    """Get the text line of an item affix.

    :return: Item affix line or False."""
    for index, line in enumerate(text):
        if line.startswith(stat):
            return index


def _item_text(text: List[str]) -> Iterator[str]:
    """Get all affixes on an item.

    :return: Generator for an item's affixes."""
    for index, line in enumerate(text):
        if line.startswith("Implicits: "):
            try:
                yield from text[index + 1 :]
            except KeyError:
                return ""


def _get_text(
    text: List[str], variant: str, alt_variant: str, mod_ranges: List[float]
) -> str:
    def _parse_text(text_, variant_, alt_variant_, mod_ranges_):
        """Get the correct variant and item affix values
            for items made in Path Of Building.

        :return: Multiline string of correct item variants and item affix values."""
        counter = 0
        # We have to advance this every time we get a line with text to replace,
        # not every time we substitute.
        for line in _item_text(text_):
            if line.startswith(
                "{variant:"
            ):  # We want to skip all mods of alternative item versions.
                item_variants = (
                    line.partition("{variant:")[-1].partition("}")[0].split(",")
                )
                if variant_ not in item_variants:
                    if alt_variant_ not in item_variants:
                        continue
            # Check for "{range:" used in range tags to filter unsupported mods.
            if "{range:" in line:
                if "Adds (" in line:
                    # "Adds (A-B) to (C-D) to something" mods need to be replaced twice.
                    value = mod_ranges_[counter]
                    line = _calculate_mod_text(line, value)
                if "(" in line:
                    value = mod_ranges_[counter]
                    line = _calculate_mod_text(line, value)
                    counter += 1
            # Omit "{variant: *}" and "{range: *}" tags.
            *_, mod = line.rpartition("}")
            yield mod

    return "\n".join(_parse_text(text, variant, alt_variant, mod_ranges))


def _calculate_mod_text(line: str, value: float) -> str:
    """Calculate an item affix's correct value from range and offset.

    :return: Corrected item affix value."""
    start, stop = line.partition("(")[-1].partition(")")[0].split("-")
    width = float(stop) - float(start) + 1
    # Python's round() function uses banker's rounding from 3.0 onwards
    # We have to emulate Path of Exile's "towards 0" rounding.
    # https://en.wikipedia.org/w/index.php?title=IEEE_754#Rounding_rules
    offset = decimal.Decimal(width * value).to_integral(decimal.ROUND_HALF_DOWN)
    result = float(start) + float(offset)
    replace_string = f"({start}-{stop})"
    result_string = f"{result if result % 1 else int(result)}"
    return line.replace(replace_string, result_string)
