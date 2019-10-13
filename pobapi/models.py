# Built-ins
from abc import ABC
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional, Tuple, Union

# Third-party
from dataslots import with_slots

__all__ = ["Gem", "GrantedAbility", "SkillGroup", "Tree", "Item", "Set"]


class Ability(ABC):
    """Abstract class that holds the data of an ability..

    :param name: Ability name.
    :param enabled: Whether the ability is in active use.
    :param level: Ability level."""

    name: str
    enabled: bool
    level: int


@with_slots
@dataclass
class Gem(Ability):
    """Class that holds the data of an ability granted by a skill gem.

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
class GrantedAbility(Ability):
    """Class that holds the data of an ability granted by an item.

    :param name: Granted ability name.
    :param enabled: Whether the granted ability is in active use.
    :param level: Granted ability level.

    .. note: Granted abilities cannot have any quality on them."""

    name: str
    enabled: bool
    level: int


@with_slots
@dataclass
class SkillGroup:
    """Class that holds a (linked) socket group.

    :param enabled: Whether the socket group is in active use.
    :param label: Socket group label assigned in Path Of Building.
    :param active: Main skill in socket group, if given.
    :param abilities: List of :class:`Gem <Gem>` or :class:`GrantedAbility <GrantedAbility>` objects in socket group."""

    enabled: bool
    label: str
    active: Optional[int]
    abilities: List[Union[Gem, GrantedAbility]]


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
class Keystones:
    """Class that holds keystone data.

    :param acrobatics: Whether the player has Acrobatics.
    :param ancestral_bond: Whether the player has Ancestral Bond.
    :param arrow_dancing: Whether the player has Arrow Dancing.
    :param avatar_of_fire: Whether the player has Avatar of Fire.
    :param blood_magic: Whether the player has Blood Magic.
    :param chaos_inoculation: Whether the player has Chaos Inoculation.
    :param conduit: Whether the player has Conduit.
    :param crimson_dance: Whether the player has Crimson Dance.
    :param eldritch_battery: Whether the player has Eldritch Battery.
    :param elemental_equilibrium: Whether the player has Elemental Equilibrium.
    :param ghost_reaver: Whether the player has Ghost Reaver.
    :param iron_grip: Whether the player has Iron Grip.
    :param iron_reflexes: Whether the player has Iron Reflexes.
    :param mind_over_matter: Whether the player has Mind Over Matter.
    :param minion_instability: Whether the player has Minion Instability.
    :param necromantic_aegis: Whether the player has Necromantic  Aegis.
    :param pain_attunement: Whether the player has Pain Attunement.
    :param perfect_agony: Whether the player has Perfect Agony.
    :param phase_acrobatics: Whether the player has Phase Acrobatics.
    :param point_blank: Whether the player has Point Blank.
    :param resolute_technique: Whether the player has Resolute Technique.
    :param runebinder: Whether the player has Runebinder.
    :param unwavering_stance: Whether the player has Unwavering Stance.
    :param vaal_pact: Whether the player has Vaal Pact.
    :param wicked_ward: Whether the player has Wicked Ward.
    :param zealots_oath: Whether the player has Zealots Oath."""

    acrobatics: bool
    ancestral_bond: bool
    arrow_dancing: bool
    avatar_of_fire: bool
    blood_magic: bool
    chaos_inoculation: bool
    conduit: bool
    crimson_dance: bool
    eldritch_battery: bool
    elemental_equilibrium: bool
    ghost_reaver: bool
    iron_grip: bool
    iron_reflexes: bool
    mind_over_matter: bool
    minion_instability: bool
    necromantic_aegis: bool
    pain_attunement: bool
    perfect_agony: bool
    phase_acrobatics: bool
    point_blank: bool
    resolute_technique: bool
    runebinder: bool
    unwavering_stance: bool
    vaal_pact: bool
    wicked_ward: bool
    zealots_oath: bool

    def __iter__(self):
        for k, v in asdict(self).items():
            if v:
                yield k


SocketGroup = Tuple[str]
GroupOfSocketGroups = Tuple[SocketGroup]


@with_slots
@dataclass
class Item:
    """Class that holds an item.

    :param rarity: Item rarity.
    :param name: Item name.
    :param base: Item base type.
    :param uid: Unique item ID for items in-game.

    .. note:: Items created in Path of Building do not have an UID.

    :param shaper: Whether the item is a Shaper base type.
    :param elder: Whether the item is an Elder base type.
    :param crafted: Whether the item has a crafted mod.
    :param quality: Item quality, if the item can have quality.
    :param sockets: Item socket groups, if the item can have sockets.

    .. note:: The format used for example a 5 socket chest armour with 2 socket groups of 3 linked blue sockets and
        2 linked red sockets would be ((B, B, B), (R, R)).

    :param level_req: Required character level to equip the item.
    :param item_level: Item level.
    :param implicit: Number of item implicits, if the item can have implicits.
    :param text: Item text.

    .. note:: For items existing in-game, their item text is just copied. For items created with Path Of Building,
        their affix values are calculated to match in-game items in appearance."""

    rarity: str
    name: str
    base: str
    uid: str
    shaper: bool
    elder: bool
    crafted: bool
    quality: Optional[int]
    sockets: Optional[GroupOfSocketGroups]
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
        if self.crafted:
            text += f"Crafted Item\n"
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
    """Set(*args)
    Class that holds an item set.

    :param weapon1: Primary weapon.
    :param weapon1_as1: Primary weapon abyssal socket 1.
    :param weapon1_as2: Primary weapon abyssal socket 1.
    :param weapon1_swap: Second primary weapon.
    :param weapon1_swap_as1: Second primary weapon abyssal socket 1.
    :param weapon1_swap_as2: Second primary weapon abyssal socket 2.
    :param weapon2: Secondary weapon.
    :param weapon2_as1: Secondary weapon abyssal socket 1.
    :param weapon2_as2: Secondary weapon abyssal socket 1.
    :param weapon2_swap: Second secondary weapon.
    :param weapon2_swap_as1: Second secondary weapon abyssal socket 1.
    :param weapon2_swap_as2: Second secondary weapon abyssal socket 2.
    :param helmet: Helmet.
    :param helmet_as1: Helmet abyssal socket 1.
    :param helmet_as2: Helmet abyssal socket 2.
    :param body_armour: Body armour.
    :param body_armour_as1: Body armour abyssal socket 1.
    :param body_armour_as2: Body armour abyssal socket 2.
    :param gloves: Gloves.
    :param gloves_as1: Gloves abyssal socket 1.
    :param gloves_as2: Gloves abyssal socket 2.
    :param boots: Boots.
    :param boots_as1: Boots abyssal socket 1.
    :param boots_as2: Boots abyssal socket 2.
    :param amulet: Amulet.
    :param ring1: Left ring.
    :param ring2: Right ring.
    :param belt: Belt.
    :param belt_as1: Belt abyssal socket 1.
    :param belt_as2: Belt abyssal socket 2.
    :param flask1: Flask bound to '1' by default.
    :param flask2: Flask bound to '2' by default.
    :param flask3: Flask bound to '3' by default.
    :param flask4: Flask bound to '4' by default.
    :param flask5: Flask bound to '5' by default."""

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
