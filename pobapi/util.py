import base64
# TODO: lxml vs. cElementTree for parsing?
import zlib
from typing import Dict, List, Iterator, Any
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


def fetch_url(url: str, timeout: float=6.0) -> str:
    if url.startswith("https://pastebin.com/"):
        try:
            raw = url.replace("https://pastebin.com/", "https://pastebin.com/raw/")
            request = requests.get(raw, timeout=timeout)
        except requests.URLRequired as e:
            raise ValueError(e, "Not a valid URL.") from e
        except requests.Timeout as e:
            print(e, "Connection timed out, try again or try raise the timeout.")
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
    if isinstance(import_code, str):
        try:
            base64_decode = base64.urlsafe_b64decode(import_code)
            decompressed_xml = zlib.decompress(base64_decode)
        except (TypeError, ValueError) as e:
            print(e, "Something went wrong while decoding. Fix it.")
        except zlib.error as e:
            print(e, "Something went wrong while decompressing. Fix it.")
        else:
            return decompressed_xml
    else:
        raise ValueError(import_code, "Import code is not a string.")


@property
def _use_second_weapon_set(self) -> bool:
    return True if self.xml.find("Items").get("useSecondWeaponSet") == "true" else False


def get_active_skill_gem(skill_group_slice):
    return skill_group_slice.gems[skill_group_slice.main - 1]


def implicit_text(text: List[str]) -> str:
    implicit = get_stat(text, "Implicits: ")
    if implicit:
        return text[_get_text_start(text, "Implicits: ") + int(implicit)]
    else:
        return "Implicits: None"


def get_stat(text: List[str], stat, default=None) -> str:
    for line in text:
        if line.startswith(stat):
            return line[len(stat):]
    return default


def _get_text_start(text: List[str], stat: Any):
    for index, line in enumerate(text):
        if line.startswith(stat):
            return index
    return 0


def item_text(text: List[str]) -> str:
    return "\n".join(text[_get_text_start(text, "Implicits: ") + int(get_stat(text, "Implicits: ", 0)):])


@property
def _current_item_set(self) -> Dict[str, int]:
    return {item.get("name"): int(item.get("itemId"))
            for item in self.xml.find("Items").find_all("Slot", recursive=0)}


@property
def _active_item_set_index(self) -> int:
    return int(self.xml.find("Items").get("activeItemSet"))


@property
def _item_sets(self) -> Iterator[Dict[str, int]]:
    for item_set in self.xml.find_all("ItemSet"):
        yield {slot.get("name"): int(slot.get("itemId")) for slot in item_set.find_all("Slot")}


if __name__ == "__main__":
    with open("../resources/import_code.txt") as f:
        code = f.read()

# pastebin.com link
# import code
# xml
