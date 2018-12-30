# Built-ins
import base64
import decimal
from typing import Iterator, List
import zlib
# Third-Party
import requests


class CachedProperty:
    def __init__(self, func):
        self.__name__ = func.__name__
        self.__module__ = func.__module__
        self.__doc__ = func.__doc__
        self._func = func

    def __get__(self, obj, cls=None):
        if obj is None:
            return self
        value = self._func(obj)
        setattr(obj, self._func.__name__, value)
        return value


def accumulate(func):
    def _accumulate_helper(*args, **kw):
        return list(func(*args, **kw))
    return _accumulate_helper


def fetch_url(url: str, timeout: float = 6.0) -> str:
    if url.startswith("https://pastebin.com/"):
        raw = url.replace("https://pastebin.com/", "https://pastebin.com/raw/")
        try:
            request = requests.get(raw, timeout=timeout)
        except requests.URLRequired as e:
            raise ValueError(e, url, "is not a valid URL.") from e
        except requests.Timeout as e:
            print(e, "Connection timed out, try again or raise the timeout.")
        except (requests.ConnectionError,
                requests.HTTPError,
                requests.RequestException,
                requests.TooManyRedirects) as e:
            print(e, "Something went wrong, check it out.")
        else:
            return fetch_import_code(request.text)
    else:
        raise ValueError(url, "is not a valid pastebin.com URL.")


def fetch_import_code(import_code: str) -> str:
    try:
        base64_decode = base64.urlsafe_b64decode(import_code)
        decompressed_xml = zlib.decompress(base64_decode)
    except (TypeError, ValueError) as e:
        print(e, "Something went wrong while decoding. Fix it.")
    except zlib.error as e:
        print(e, "Something went wrong while decompressing. Fix it.")
    else:
        return decompressed_xml


@accumulate
def _nodes(url):
    bin_tree = base64.urlsafe_b64decode(url)
    position = 7
    while position < len(bin_tree) - 1:
        yield int.from_bytes(bin_tree[position:position + 2], byteorder='big')
        position += 2


def _get_stat(text: List[str], stat: str, default=None) -> str:
    for line in text:
        if line.startswith(stat):
            _, _, result = line.partition(stat)
            return result
    return default


def _item_text(text: List[str]) -> Iterator[str]:
    for index, line in enumerate(text):
        if line.startswith("Implicits: "):
            try:
                yield from text[index + 1:]
            except KeyError:
                return ""


def _text_parse(text: Iterator[str], variant: str, alt_variant: str, mod_ranges: List[float]) -> Iterator[str]:
    counter = 0  # We have to advance this every time we get a line with text to replace, not every time we substitute.
    for line in text:
        if line.startswith("{variant:"):  # We want to skip all mods of alternative item versions.
            if variant not in line.partition("{variant:")[-1].partition("}")[0].split(","):
                if alt_variant not in line.partition("{variant:")[-1].partition("}")[0].split(","):
                    continue
        # We have to check for '{range:' used in range tags to filter unsupported mods.
        if "Adds (" in line and "{range:" in line:  # 'Adds (A-B) to (C-D) to something' mods need to be replaced twice.
            value = mod_ranges[counter]
            line = _calculate_mod_text(line, value)
        if "(" in line and "{range:" in line:
            value = mod_ranges[counter]
            line = _calculate_mod_text(line, value)
            counter += 1
        # We are only interested in everything past the '{variant: *}' and '{range: *}' tags.
        _, _, mod = line.rpartition("}")
        yield mod


def _calculate_mod_text(line: str, value: float) -> str:
    start, stop = line.partition("(")[-1].partition(")")[0].split("-")
    width = float(stop) - float(start) + 1
    # Python's round() function uses banker's rounding from 3.0 onwards, we have to emulate Lua's 'towards 0' rounding.
    # https://en.wikipedia.org/w/index.php?title=IEEE_754#Rounding_rules
    offset = decimal.Decimal(width * value).to_integral(decimal.ROUND_HALF_DOWN)
    result = float(start) + float(offset)
    replace_string = f"({start}-{stop})"
    result_string = f"{result if result % 1 else int(result)}"
    return line.replace(replace_string, result_string)
