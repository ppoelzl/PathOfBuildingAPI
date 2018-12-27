# Built-ins
from dataclasses import dataclass
from typing import Dict, List, Tuple, Union

__all__ = ["Gem", "Skill", "Tree", "Item"]


@dataclass
class Gem:
    name: str
    enabled: bool
    level: int
    quality: int


@dataclass
class Skill:
    enabled: bool
    label: str
    active: Union[int, None]
    gems: List[Gem]


@dataclass
class Tree:
    url: str
    sockets: Dict[int, int]


@dataclass
class Item:
    rarity: str
    name: str
    base: str
    uid: str
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


@dataclass
class Set:
    weapon1: int
    weapon1_as1: int
    weapon1_as2: int
    weapon1_swap: int
    weapon1_swap_as1: int
    weapon1_swap_as2: int
    weapon2: int
    weapon2_as1: int
    weapon2_as2: int
    weapon2_swap: int
    weapon2_swap_as1: int
    weapon2_swap_as2: int
    helmet: int
    helmet_as1: int
    helmet_as2: int
    body_armour: int
    body_armour_as1: int
    body_armour_as2: int
    gloves: int
    gloves_as1: int
    gloves_as2: int
    boots: int
    boots_as1: int
    boots_as2: int
    amulet: int
    ring1: int
    ring2: int
    belt: int
    belt_as1: int
    belt_as2: int
    flask1: int
    flask2: int
    flask3: int
    flask4: int
    flask5: int
