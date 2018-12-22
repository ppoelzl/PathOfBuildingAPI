# Built-ins
from dataclasses import dataclass
from typing import Dict, List, Tuple, Union

__all__ = ["Gems", "Skill", "Tree", "Item"]


@dataclass
class Gems:
    name: str
    enabled: bool
    level: int
    quality: int


@dataclass
class Skill:
    enabled: bool
    label: str
    active: Union[int, None]
    gems: List[Gems]


@dataclass
class Tree:
    url: str
    sockets: Dict[int, int]


@dataclass
class Item:
    rarity: str
    name: str
    base: str
    shaper: bool
    elder: bool
    quality: Union[int, None]
    sockets: Union[Tuple[str], None]
    level_req: int
    item_level: int
    implicit: Union[int, None]
    text: str

    def __str__(self):
        text = ""
        text += f"Rarity: {self.rarity}\n"
        text += f"Name: {self.name}\n"
        text += f"Base: {self.base}\n"
        if self.shaper:
            text += f"Shaper Item\n"
        if self.elder:
            text += f"Elder Item\n"
        if self.quality:
            text += f"Quality: {self.quality}\n"
        if self.sockets:
            text += f"Sockets: {self.sockets}\n"
        text += f"LevelReq: {self.level_req}\n"
        text += f"ItemLvl: {self.item_level}\n"
        if self.implicit:
            text += f"Implicits: {self.implicit}\n"
        text += f"{self.text}"
        return text
