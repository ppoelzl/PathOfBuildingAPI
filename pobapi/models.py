# Built-ins
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
# Third-party
from dataslots import with_slots
__all__ = ["Gem", "Skill", "Tree", "Item", "Set"]


@with_slots
@dataclass
class Gem:
    """Class that holds a skill gem's data.

    :param name: Skill gem name.
    :param enabled: Whether the skill gem is in active use.
    :param level: Skill gem level.
    :param quality: Skill gem quality."""
    name: str
    enabled: bool
    level: int
    quality: int


@with_slots
@dataclass
class Skill:
    """Class that holds a (linked) socket group.

    :param enabled: Whether the socket group is in active use.
    :param label: Socket group label assigned in Path Of Building.
    :param active: Main skill in socket group, if given.
    :param gems: List of :class:`Gem <Gem>` objects in socket group."""
    enabled: bool
    label: str
    active: Optional[int]
    gems: List[Gem]


@with_slots
@dataclass
class Tree:
    """Class that holds a passive skill tree.

    :param url: pathofexile.com link to passive skill tree.
    :param nodes: List of passive skill tree nodes by ID.
    :param sockets: Dictionary of passive skill tree jewel socket location : jewel set ID."""
    url: str
    nodes: List[int]
    sockets: Dict[int, int]


@with_slots
@dataclass
class Item:
    """Class that holds an item.

    :param rarity: Item rarity.
    :param name: Item name.
    :param base: Item base type.
    :param uid: Unique item ID for items in-game.
    Note: Items created with Path of Building do not have an UID.
    :param shaper: Whether the item is a Shaper base type.
    :param elder: Whether the item is an Elder base type.
    :param quality: Item quality, if the item can have quality.
    :param sockets: Item socket groups, if the item can have sockets.
    Note: The format used for example a 5 socket chest armour with 2 socket groups of 3 linked blue sockets and 2 linked
    red sockets would be ((B, B, B), (R, R)).
    :param level_req: Required character level to equip the item.
    :param item_level: Item level.
    :param implicit: Number of item implicits, if the item can have implicits.
    :param text: Item text.
    Note: For items existing in-game, their item text is just copied. For items created with Path Of Building, their
    affix values are calculated to match in-game items in appearance."""
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


@with_slots
@dataclass
class Set:
    """Class that holds an item set."""
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
