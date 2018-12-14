# Built-ins
from __future__ import annotations
from dataclasses import dataclass, InitVar
import decimal
import re
from typing import Dict, Iterator, List, Tuple, Union
# Project
from pobapi.constants import CONFIG_MAP, STATS_MAP, MONSTER_DAMAGE_TABLE, MONSTER_LIFE_TABLE
from pobapi import util
# Third-Party
from defusedxml import lxml

"""API Provider for PathOfBuilding's XML export format."""

__all__ = ["PathOfBuildingAPI"]


@dataclass
class GeneralConfig:
    resistance_penalty: int = -60  # val = (0, -30, nil) -60 is default if omitted
    enemy_level: int = None
    enemy_physical_hit_damage: float = None
    detonate_dead_corpse_life: int = None
    is_stationary: bool = False
    is_moving: bool = False
    on_full_life: bool = False
    on_low_life: bool = False
    on_full_energy_shield: bool = False
    has_energy_shield: bool = False
    minions_on_full_life: bool = False
    ignite_mode: str = None  # val = (Average / Crit)


@dataclass
class SkillConfig:
    aspect_of_the_avian_avians_might: bool = False
    aspect_of_the_avian_avians_flight: bool = False
    aspect_of_the_cat_cats_stealth: bool = False
    aspect_of_the_cat_cats_agility: bool = False
    override_crab_barriers: int = None
    aspect_of_the_spider_web_stacks: int = None
    dark_pact_skeleton_life: int = None
    ice_nova_cast_on_frostbolt: bool = False
    innervate_innervation: bool = False
    raise_spectres_spectre_level: int = None
    siphoning_trap_affected_enemies: int = None
    raise_spectres_enable_curses: bool = False
    raise_spectres_blade_vortex_blade_count: int = None
    summon_lightning_golem_enable_wrath: bool = False
    vortex_cast_on_frostbolt: bool = False


@dataclass
class MapConfig:
    enemy_physical_reduction: int = None  # l:20%/m:30%/h:40%
    enemy_hexproof: bool = False
    less_curse_effect: int = None  # l:25%/m:40%/h:60%
    enemy_avoid_poison_blind_bleed: int = None  # l:25%/m:45%/h:65%
    enemy_resistances: str = False  # map = { ["Low"] = {20,15}, ["Mid"] = {30,20}, ["High"] = {40,25} } (ele, chaos)
    elemental_equilibrium: bool = False
    no_leech: bool = False
    reduced_flask_charges: int = None  # l:30%/m:40%/h:50%
    minus_max_resists: int = None  # m:5-8%/h:9-12%
    less_aoe: int = None  # l:15%/m:20%/h:25%
    enemy_avoid_status_ailment: int = None  # l:30%/m:60%/h:90%
    enemy_increased_accuracy: int = None  # l:30%/m:40%/h:50%
    less_armour_block: str = None  # map = { ["LOW"] = {20,20}, ["MID"] = {30,25}, ["HIGH"] = {40,30} } (block, armour)
    point_blank: bool = False
    less_recovery: int = None  # l:20%/m:40%/h:60%
    no_regen: bool = False
    enemy_takes_reduced_extra_crit_damage: int = None  # l:25-30%/m:31-35%/h:36-40%
    curse_assassins_mark: int = None  # level
    curse_conductivity: int = None  # level
    curse_despair: int = None  # level
    curse_elemental_weakness: int = None  # level
    curse_enfeeble: int = None  # level
    curse_flammability: int = None  # level
    curse_frostbite: int = None  # level
    curse_poachers_mark: int = None  # level
    curse_projectile_weakness: int = None  # level
    curse_punishment: int = None  # level
    curse_temporal_chains: int = None  # level
    curse_vulnerability: int = None  # level
    curse_warlords_mark: int = None  # level


@dataclass
class CombatConfig:
    use_power_charges: bool = False
    max_power_charges: int = None
    use_frenzy_charges: bool = False
    max_frenzy_charges: int = None
    use_endurance_charges: bool = False
    max_endurance_charges: int = None
    use_siphoning_charges: bool = False
    max_siphoning_charges: int = None
    minions_use_power_charges: bool = False
    minions_use_frenzy_charges: bool = False
    minions_use_endurance_charges: bool = False
    onslaught: bool = False
    unholy_might: bool = False
    phasing: bool = False
    fortify: bool = False
    tailwind: bool = False
    adrenaline: bool = False
    rage: bool = False
    leeching: bool = False
    using_flask: bool = False
    has_totem: bool = False
    on_consecrated_ground: bool = False
    on_burning_ground: bool = False
    on_chilled_ground: bool = False
    on_shocked_ground: bool = False
    burning: bool = False
    ignited: bool = False
    chilled: bool = False
    frozen: bool = False
    shocked: bool = False
    bleeding: bool = False
    poisoned: bool = False
    number_of_poison_stacks: int = None
    only_one_nearby_enemy: bool = False
    hit_recently: bool = False
    crit_recently: bool = False
    killed_recently: bool = False
    number_of_enemies_killed_recently: int = None
    totems_killed_recently: bool = False
    number_of_totems_killed_recently: int = None
    minions_killed_recently: bool = False
    number_of_minions_killed_recently: int = None
    killed_affected_by_dot: bool = False
    number_of_shocked_enemies_killed_recently: int = None
    frozen_enemy_recently: bool = False
    shattered_enemy_recently: bool = False
    ignited_enemy_recently: bool = False
    shocked_enemy_recently: bool = False
    number_of_poisons_applied_recently: int = None
    been_hit_recently: bool = False
    been_crit_recently: bool = False
    been_savage_hit_recently: bool = False
    hit_by_fire_damage_recently: bool = False
    hit_by_cold_damage_recently: bool = False
    hit_by_lightning_damage_recently: bool = False
    blocked_recently: bool = False
    blocked_attack_recently: bool = False
    blocked_spell_recently: bool = False
    energy_shield_recharge_started_recently: bool = False
    pendulum_of_destruction: str = False  # val = (Area / Damage)
    elemental_conflux: str = False  # val = (Chilling / Shocking / Igniting / All)
    bastion_of_hope: bool = False
    her_embrace: bool = False
    used_skill_recently: bool = False
    attacked_recently: bool = False
    cast_spell_recently: bool = False
    used_fire_skill_recently: bool = False
    used_cold_skill_recently: bool = False
    used_minion_skill_recently: bool = False
    used_movement_skill_recently: bool = False
    used_vaal_skill_recently: bool = False
    used_warcry_recently: bool = False
    number_of_mines_detonated_recently: int = None
    number_of_traps_triggered_recently: int = None
    consumed_corpses_recently: bool = False
    number_of_corpses_consumed_recently: int = None
    taunted_enemy_recently: bool = False
    blocked_hit_from_unique_enemy_in_past_ten_seconds: bool = False


@dataclass
class DPSOptions:
    lucky_crits: bool = False
    number_of_times_skill_has_chained: int = None
    projectile_distance: int = None
    enemy_in_close_range: bool = False
    enemy_moving: bool = False
    enemy_on_full_life: bool = False
    enemy_on_low_life: bool = False
    enemy_cursed: bool = False
    enemy_bleeding: bool = False
    enemy_poisoned: bool = False
    enemy_number_of_poison_stacks: int = None
    enemy_maimed: bool = False
    enemy_hindered: bool = False
    enemy_blinded: bool = False
    enemy_taunted: bool = False
    enemy_burning: bool = False
    enemy_ignited: bool = False
    enemy_chilled: bool = False
    enemy_frozen: bool = False
    enemy_shocked: bool = False
    enemy_number_of_freeze_shock_ignite: int = None
    enemy_intimidated: bool = False
    enemy_covered_in_ash: bool = False
    enemy_rare_or_unique: bool = False
    enemy_boss: bool = False  # val = (False / True / Shaper)
    enemy_physical_damage_reduction: int = None
    enemy_fire_resist: int = None
    enemy_cold_resist: int = None
    enemy_lightning_resist: int = None
    enemy_chaos_resist: int = None
    enemy_hit_by_fire_damage: bool = False
    enemy_hit_by_cold_damage: bool = False
    enemy_hit_by_lightning_damage: bool = False
    elemental_equilibrium_ignore_hit_damage: bool = False


@dataclass
class Config(GeneralConfig, SkillConfig, MapConfig, CombatConfig, DPSOptions):
    character_level: InitVar[int] = None

    def __post_init__(self, character_level: int):
        if self.enemy_level is None:
            self.enemy_level = min(character_level, 84)
        if self.enemy_physical_hit_damage is None:
            self.enemy_physical_hit_damage = MONSTER_DAMAGE_TABLE[self.enemy_level - 1] * 1.5
        if self.detonate_dead_corpse_life is None:
            self.detonate_dead_corpse_life = MONSTER_LIFE_TABLE[self.enemy_level - 1]


@dataclass
class Gems:
    name: str
    enabled: bool
    level: int
    quality: int


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


@dataclass
class Skill:
    enabled: bool
    label: str
    active: Union[int, None]
    gems: List[Gems]


@dataclass
class Stats:
    average_hit: float = None
    average_damage: float = None
    cast_speed: float = None
    attack_speed: float = None
    trap_throwing_speed: float = None
    trap_cooldown: float = None
    mine_laying_speed: float = None
    totem_placement_speed: float = None
    pre_effective_crit_chance: float = None
    crit_chance: float = None
    crit_multiplier: float = None
    hit_chance: int = None
    total_dps: float = None
    total_dot: float = None
    bleed_dps: float = None
    ignite_dps: float = None
    ignite_damage: float = None
    total_dps_with_ignite: float = None
    average_damage_with_ignite: float = None
    poison_dps: float = None
    poison_damage: float = None
    total_dps_with_poison: float = None
    average_damage_with_poison: float = None
    decay_dps: float = None
    skill_cooldown: float = None
    area_of_effect_radius: float = None
    mana_cost: float = None
    strength: float = None
    strength_required: float = None
    dexterity: float = None
    dexterity_required: float = None
    intelligence: float = None
    intelligence_required: float = None
    life: float = None
    life_increased: float = None
    life_unreserved: float = None
    life_unreserved_percent: float = None
    life_regen: float = None
    life_leech_rate_per_hit: float = None
    life_leech_gain_per_hit: float = None
    mana: float = None
    mana_increased: float = None
    mana_unreserved: float = None
    mana_unreserved_percent: float = None
    mana_regen: float = None
    mana_leech_rate_per_hit: float = None
    mana_leech_gain_per_hit: float = None
    total_degen: float = None
    net_life_regen: float = None
    net_mana_regen: float = None
    energy_shield: float = None
    energy_shield_increased: float = None
    energy_shield_regen: float = None
    energy_shield_leech_rate_per_hit: float = None
    energy_shield_leech_gain_per_hit: float = None
    evasion: float = None
    evasion_increased: float = None
    melee_evade_chance: float = None
    melee_evade_chance2: float = None
    projectile_evade_chance: float = None
    armour: float = None
    armour_increased: float = None
    physical_damage_reduction: float = None
    effective_movement_speed_modifier: float = None
    block_chance: float = None
    spell_block_chance: float = None
    attack_dodge_chance: float = None
    spell_dodge_chance: float = None
    fire_resistance: float = None
    cold_resistance: float = None
    lightning_resistance: float = None
    chaos_resistance: float = None
    fire_resistance_over_cap: float = None
    cold_resistance_over_cap: float = None
    lightning_resistance_over_cap: float = None
    chaos_resistance_over_cap: float = None
    power_charges: float = None
    power_charges_maximum: float = None
    frenzy_charges: float = None
    frenzy_charges_maximum: float = None
    endurance_charges: float = None
    endurance_charges_maximum: float = None
    active_totem_limit: float = None
    active_minion_limit: float = None


@dataclass
class Tree:
    url: str
    sockets: Dict[int: int]


class PathOfBuildingAPI:
    def __init__(self, xml: str):
        self.xml = lxml.fromstring(xml)

    @classmethod
    def from_url(cls, url: str) -> PathOfBuildingAPI:
        return cls(util.fetch_url(url))

    @classmethod
    def from_import_code(cls, import_code: str) -> PathOfBuildingAPI:
        return cls(util.fetch_import_code(import_code))

    #

    @util.CachedProperty
    def stats(self) -> Stats:
        kwargs = {STATS_MAP[i.get("stat")]: float(i.get("value")) for i in self.xml.find("Build").findall("PlayerStat")}
        return Stats(**kwargs)

    @util.CachedProperty
    def skill_groups(self) -> List[Skill]:
        return [_skill_builder(skill) for skill in self.xml.find("Skills").findall("Skill")]

    @util.CachedProperty
    def items(self) -> List[Item]:
        return [_item_builder(item) for item in self.xml.find("Items").findall("Item")]

    @util.CachedProperty
    def trees(self) -> List[Tree]:
        return [_tree_builder(spec) for spec in self.xml.find("Tree").findall("Spec")]

    @util.CachedProperty
    def config(self) -> Config:
        kwargs = {CONFIG_MAP[i.get("name")]: _convert_fields(i) for i in self.xml.find("Config").findall("Input")}
        kwargs["character_level"] = self.level
        return Config(**kwargs)

    @util.CachedProperty
    def class_name(self) -> str:
        return self.xml.find("Build").get("className")

    @util.CachedProperty
    def ascendancy_name(self) -> Union[str, None]:
        return self.xml.find("Build").get("ascendClassName")

    @util.CachedProperty
    def level(self) -> int:
        return int(self.xml.find("Build").get("level"))

    @util.CachedProperty
    def bandit(self) -> Union[str, None]:
        return self.xml.find("Build").get("bandit")

    @util.CachedProperty
    def notes(self) -> str:
        return self.xml.find("Notes").text.rstrip("\n\r\t")

    @util.CachedProperty
    def second_weapon_set(self) -> bool:
        return True if self.xml.find("Items").get("useSecondWeaponSet") == "true" else False

    @util.CachedProperty
    def item_sets(self) -> Iterator[Dict[str, int]]:
        for item_set in self.xml.find_all("ItemSet"):
            yield {slot.get("name"): int(slot.get("itemId")) for slot in item_set.find_all("Slot")}

    @util.CachedProperty
    def current_item_set(self) -> Dict[str, int]:
        return {item.get("name"): int(item.get("itemId"))
                for item in self.xml.find("Items").find_all("Slot", recursive=0)}

    @util.CachedProperty
    def current_item_set_index(self) -> int:
        return int(self.xml.find("Items").get("activeItemSet"))

    @util.CachedProperty
    def active_skill_group(self) -> Skill:
        index = int(self.xml.find("Build").get("mainSocketGroup")) - 1
        return self.skill_groups[index]

    @util.CachedProperty
    def active_skill(self) -> Gems:
        index = self.active_skill_group.active - 1
        return self.active_skill_group.gems[index]

    @util.CachedProperty
    def active_skill_tree(self) -> Tree:
        index = int(self.xml.find("Tree").get("activeSpec")) - 1
        return self.trees[index]

    @util.CachedProperty
    def skill_gems(self) -> List[Gems]:
        return [gem for group in self.skill_groups for gem in group.gems]

    @util.CachedProperty
    def skill_names(self) -> List[str]:
        return [gem.get("nameSpec") for gem in self.xml.findall("Gem")]


def _skill_builder(skill: lxml.RestrictedElement) -> Skill:
    enabled = True if skill.get("enabled") == "true" else False
    label = skill.get("label")
    active = int(skill.get("mainActiveSkill")) if not skill.get("mainActiveSkill") == "nil" else None
    gems = [_gem_builder(gem) for gem in skill.findall("Gem")]
    return Skill(enabled, label, active, gems)


def _gem_builder(gem: lxml.RestrictedElement) -> Gems:
    name = gem.get("nameSpec")
    enabled = True if gem.get("enabled") == "true" else False
    level = int(gem.get("level"))
    quality = int(gem.get("quality"))
    return Gems(name, enabled, level, quality)


def _item_builder(text: lxml.RestrictedElement) -> Item:  # TODO: Cleanup
    _variant = text.get("variantAlt")
    if not _variant:
        _variant = text.get("variant")
    _mod_ranges = [float(i.get("range")) for i in text.findall("ModRange")]
    item = text.text.strip("\n\r\t").splitlines()
    rarity = util.get_stat(item, "Rarity: ").capitalize()
    name = item[1]
    base = item[1] if item[2].startswith(("Crafted: true", "Unique ID:")) else item[2]
    shaper = True if util.get_stat(item, "Shaper Item") else False
    elder = True if util.get_stat(item, "Elder Item") else False
    quality = int(util.get_stat(item, "Quality: ", default=0)) or None
    sockets = util.get_stat(item, "Sockets: ")
    if sockets:
        sockets = tuple(sockets.split("-"))
    level_req = int(util.get_stat(item, "Item Level: ", default=1))
    item_level = int(util.get_stat(item, "Item Level: ", default=1))
    implicit = int(util.get_stat(item, "Implicits: "))
    item_text = _text_parse(util.item_text(item), _variant, _mod_ranges)
    return Item(rarity, name, base, shaper, elder, quality, sockets, level_req, item_level, implicit, item_text)


def _tree_builder(spec: lxml.RestrictedElement) -> Tree:
    url = spec.find("URL").text.strip("\n\r\t")
    sockets = {int(s.get("nodeId")): int(s.get("itemId")) for s in spec.findall("Socket")}
    return Tree(url, sockets)


def _convert_fields(item: lxml.RestrictedElement) -> Union[True, int, str]:
    if item.get("boolean"):
        return True
    elif item.get("number"):
        return int(item.get("number"))
    elif item.get("string"):
        return item.get("string").capitalize()


def _text_parse(t, variant, mod_ranges):  # TODO: Cleanup
    mods = []
    counter = 0
    re_find_variant = re.compile("(?<={variant:).+?(?=})")
    for i in t.splitlines():
        if "Adds (" in i:
            start1, stop1 = i.split("(")[1].split(")")[0].split("-")
            start2, stop2 = i.rsplit("(")[1].rsplit(")")[0].split("-")
            value1 = mod_ranges[counter]
            counter += 1
            width1 = float(stop1) - float(start1) + 1
            offset1 = decimal.Decimal(width1 * value1).to_integral(decimal.ROUND_HALF_DOWN)
            result1 = float(start1) + float(offset1)
            value2 = mod_ranges[counter]
            counter += 1
            width2 = float(stop2) - float(start2) + 1
            offset2 = decimal.Decimal(width2 * value2).to_integral(decimal.ROUND_HALF_DOWN)
            result2 = float(start2) + float(offset2)
            replace_string = "(" + start1 + "-" + stop1 + ") to (" + start2 + "-" + stop2 + ")"
            result_string = str(result1 if result1 % 1 else (int(result1))) + " to " + \
                str(result2 if result2 % 1 else (int(result2)))
            i = i.replace(replace_string, result_string)
        elif "(" in i or ")" in i:
            start, stop = i.split("(")[1].split(")")[0].split("-")
            value = mod_ranges[counter]
            counter += 1
            width = float(stop) - float(start) + 1
            offset = decimal.Decimal(width * value).to_integral(decimal.ROUND_HALF_DOWN)
            result = float(start) + float(offset)
            replace_string = "(" + start + "-" + stop + ")"
            i = i.replace(replace_string, str(result if result % 1 else int(result)))
        if i.startswith(f"{{variant:"):
            exp = re.search(re_find_variant, i).group()
            sp = [int(i) for i in exp.split(",")]
            if int(variant) in sp:
                mods.append(i.rsplit("}", maxsplit=1)[1])
        elif i.startswith(f"{{range:"):
            mods.append(i.rsplit("}", maxsplit=1)[1])
        else:
            mods.append(i)

    return "\n".join(mods)
