# Built-ins
import base64
from typing import List
import zlib
# Third-Party
import requests
# TODO: lxml vs. cElementTree for parsing?


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


def fetch_url(url: str, timeout: float=6.0) -> str:
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


def fetch_import_code(import_code: str) -> str:  # TODO: XML schema validation?
    try:
        base64_decode = base64.urlsafe_b64decode(import_code)
        decompressed_xml = zlib.decompress(base64_decode)
    except (TypeError, ValueError) as e:
        print(e, "Something went wrong while decoding. Fix it.")
    except zlib.error as e:
        print(e, "Something went wrong while decompressing. Fix it.")
    else:
        return decompressed_xml


def get_stat(text: List[str], stat, default=None) -> str:
    for line in text:
        if line.startswith(stat):
            return line[len(stat):]
    return default


def item_text(text: List[str]) -> str:
    for index, line in enumerate(text):
        if line.startswith("Implicits: "):
            try:
                return "\n".join(text[index + 1:])
            except KeyError:
                return ""
