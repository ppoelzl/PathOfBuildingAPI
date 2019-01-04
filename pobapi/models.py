# Built-ins
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple

__all__ = ["Gem", "Skill", "Tree", "Item", "Set"]


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
    active: Optional[int]
    gems: List[Gem]


@dataclass
class Tree:
    url: str
    nodes: List[int]
    sockets: Dict[int, int]


@dataclass
class Item:
    rarity: str
    name: str
    base: str
    uid: str
    shaper: bool
    elder: bool
    quality: Optional[int]
    sockets: Optional[Tuple[str]]
    level_req: int
    item_level: int
    implicit: Optional[int]
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
    weapon1: Optional[int]
    weapon1_as1: Optional[int]
    weapon1_as2: Optional[int]
    weapon1_swap: Optional[int]
    weapon1_swap_as1: Optional[int]
    weapon1_swap_as2: Optional[int]
    weapon2: Optional[int]
    weapon2_as1: Optional[int]
    weapon2_as2: Optional[int]
    weapon2_swap: Optional[int]
    weapon2_swap_as1: Optional[int]
    weapon2_swap_as2: Optional[int]
    helmet: Optional[int]
    helmet_as1: Optional[int]
    helmet_as2: Optional[int]
    body_armour: Optional[int]
    body_armour_as1: Optional[int]
    body_armour_as2: Optional[int]
    gloves: Optional[int]
    gloves_as1: Optional[int]
    gloves_as2: Optional[int]
    boots: Optional[int]
    boots_as1: Optional[int]
    boots_as2: Optional[int]
    amulet: Optional[int]
    ring1: Optional[int]
    ring2: Optional[int]
    belt: Optional[int]
    belt_as1: Optional[int]
    belt_as2: Optional[int]
    flask1: Optional[int]
    flask2: Optional[int]
    flask3: Optional[int]
    flask4: Optional[int]
    flask5: Optional[int]
