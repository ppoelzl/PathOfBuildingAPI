# Built-ins
import base64
import decimal
import struct
from typing import Any, Callable, Iterator, List
import zlib

# Project
from pobapi.constants import TREE_OFFSET

# Third-party
import requests


class CachedProperty:
    """Used as a decorator for caching properties. Works like the built-in @property decorator, except that a result is
    computed on first access only, with subsequent access returning the computed result directly.
    Note that the result replaces the decorated function on first access.

    :return: Cached result."""

    def __init__(self, func: Callable):
        self.__name__ = func.__name__
        # self.__module__ = func.__module__
        # __module__ not yet implemented for collections.abc.Callable
        self.__doc__ = func.__doc__
        self._func = func

    def __get__(self, obj: Callable, cls: Callable = None) -> Any:
        if obj is None:
            return self
        value = self._func(obj)
        setattr(obj, self._func.__name__, value)
        return value


def accumulate(func: Callable) -> Callable:
    """Used as a decorator to accumulate the results a generator yields into a list.
    Note that this is useful for list comprehensions that are cleaner written with a generator approach.

    :return: Generator results."""

    def _accumulate_helper(*args, **kwargs) -> List:
        return list(func(*args, **kwargs))

    return _accumulate_helper


def fetch_xml_from_url(url: str, timeout: float = 6.0) -> str:
    """Get a Path Of Building import code shared with pastebin.com.

    :return: Decompressed XML build document."""
    if url.startswith("https://pastebin.com/"):
        raw = url.replace("https://pastebin.com/", "https://pastebin.com/raw/")
        try:
            request = requests.get(raw, timeout=timeout)
        except requests.URLRequired as e:
            raise ValueError(e, url, "is not a valid URL.") from e
        except requests.Timeout as e:
            print(e, "Connection timed out, try again or raise the timeout.")
        except (
            requests.ConnectionError,
            requests.HTTPError,
            requests.RequestException,
            requests.TooManyRedirects,
        ) as e:
            print(e, "Something went wrong, check it out.")
        else:
            return fetch_xml_from_import_code(request.text)
    else:
        raise ValueError(url, "is not a valid pastebin.com URL.")


def fetch_xml_from_import_code(import_code: str) -> str:
    """Decodes and unzips a Path Of Building import code.

    :return: Decompressed XML build document."""
    try:
        base64_decode = base64.urlsafe_b64decode(import_code)
        print(base64_decode)
        decompressed_xml = zlib.decompress(base64_decode)
    except (TypeError, ValueError) as e:
        print(e, "Something went wrong while decoding. Fix it.")
    except zlib.error as e:
        print(e, "Something went wrong while decompressing. Fix it.")
    else:
        return decompressed_xml


def _skill_tree_nodes(url: str) -> List[int]:
    """Get a list of passive tree node IDs.

    :return: Passive tree node IDs."""
    bin_tree = base64.urlsafe_b64decode(url)
    return list(
        struct.unpack_from(
            "!" + "H" * ((len(bin_tree) - TREE_OFFSET) // 2),
            bin_tree,
            offset=TREE_OFFSET,
        )
    )


def _get_stat(text: List[str], stat: str) -> str:
    """Get the value of an item affix.

    :return: Item affix value."""
    for line in text:
        if line.startswith(stat):
            _, _, result = line.partition(stat)
            return result


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
        """Get the correct variant and item affix values for items made in Path Of Building.

        :return: Multiline string of correct item variants and item affix values."""
        counter = 0
        # We have to advance this every time we get a line with text to replace, not every time we substitute.
        for line in _item_text(text_):
            if line.startswith(
                "{variant:"
            ):  # We want to skip all mods of alternative item versions.
                if variant_ not in line.partition("{variant:")[-1].partition("}")[
                    0
                ].split(","):
                    if alt_variant_ not in line.partition("{variant:")[-1].partition(
                        "}"
                    )[0].split(","):
                        continue
            # We have to check for '{range:' used in range tags to filter unsupported mods.
            if "Adds (" in line and "{range:" in line:
                # 'Adds (A-B) to (C-D) to something' mods need to be replaced twice.
                value = mod_ranges_[counter]
                line = _calculate_mod_text(line, value)
            if "(" in line and "{range:" in line:
                value = mod_ranges_[counter]
                line = _calculate_mod_text(line, value)
                counter += 1
            # We are only interested in everything past the '{variant: *}' and '{range: *}' tags.
            _, _, mod = line.rpartition("}")
            yield mod

    return "\n".join(_parse_text(text, variant, alt_variant, mod_ranges))


def _calculate_mod_text(line: str, value: float) -> str:
    """Calculate an item affix's correct value from range and offset.

    :return: Corrected item affix value."""
    start, stop = line.partition("(")[-1].partition(")")[0].split("-")
    width = float(stop) - float(start) + 1
    # Python's round() function uses banker's rounding from 3.0 onwards, we have to emulate Lua's 'towards 0' rounding.
    # https://en.wikipedia.org/w/index.php?title=IEEE_754#Rounding_rules
    offset = decimal.Decimal(width * value).to_integral(decimal.ROUND_HALF_DOWN)
    result = float(start) + float(offset)
    replace_string = f"({start}-{stop})"
    result_string = f"{result if result % 1 else int(result)}"
    return line.replace(replace_string, result_string)
