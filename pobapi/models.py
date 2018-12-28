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
    weapon1: Union[int, None]
    weapon1_as1: Union[int, None]
    weapon1_as2: Union[int, None]
    weapon1_swap: Union[int, None]
    weapon1_swap_as1: Union[int, None]
    weapon1_swap_as2: Union[int, None]
    weapon2: Union[int, None]
    weapon2_as1: Union[int, None]
    weapon2_as2: Union[int, None]
    weapon2_swap: Union[int, None]
    weapon2_swap_as1: Union[int, None]
    weapon2_swap_as2: Union[int, None]
    helmet: Union[int, None]
    helmet_as1: Union[int, None]
    helmet_as2: Union[int, None]
    body_armour: Union[int, None]
    body_armour_as1: Union[int, None]
    body_armour_as2: Union[int, None]
    gloves: Union[int, None]
    gloves_as1: Union[int, None]
    gloves_as2: Union[int, None]
    boots: Union[int, None]
    boots_as1: Union[int, None]
    boots_as2: Union[int, None]
    amulet: Union[int, None]
    ring1: Union[int, None]
    ring2: Union[int, None]
    belt: Union[int, None]
    belt_as1: Union[int, None]
    belt_as2: Union[int, None]
    flask1: Union[int, None]
    flask2: Union[int, None]
    flask3: Union[int, None]
    flask4: Union[int, None]
    flask5: Union[int, None]
