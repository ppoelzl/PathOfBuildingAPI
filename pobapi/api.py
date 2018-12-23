# Built-ins
from __future__ import annotations
from typing import Dict, Iterator, List, Union
# Project
from pobapi.constants import CONFIG_MAP, STATS_MAP
from pobapi import config
from pobapi import models
from pobapi import stats
from pobapi import util
# Third-Party
from defusedxml import lxml

"""API Provider for PathOfBuilding's XML export format."""

__all__ = ["PathOfBuildingAPI"]


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
    def active_skill_group(self) -> models.Skill:
        index = int(self.xml.find("Build").get("mainSocketGroup")) - 1
        return self.skill_groups[index]

    @util.CachedProperty
    def stats(self) -> stats.Stats:
        kwargs = {STATS_MAP[i.get("stat")]: float(i.get("value")) for i in self.xml.find("Build").findall("PlayerStat")}
        return stats.Stats(**kwargs)

    @util.CachedProperty
    @util.accumulate
    def skill_groups(self) -> Iterator[models.Skill]:
        def _gems(skill_):
            for gem in skill_:
                name = gem.get("nameSpec")
                enabled_ = True if gem.get("enabled") == "true" else False
                level = int(gem.get("level"))
                quality = int(gem.get("quality"))
                yield models.Gems(name, enabled_, level, quality)
        for skill in self.xml.find("Skills").findall("Skill"):
            enabled = True if skill.get("enabled") == "true" else False
            label = skill.get("label")
            active = int(skill.get("mainActiveSkill")) if not skill.get("mainActiveSkill") == "nil" else None
            gems = list(_gems(skill))
            yield models.Skill(enabled, label, active, gems)

    @util.CachedProperty
    def active_skill(self) -> models.Gems:
        index = self.active_skill_group.active - 1
        return self.active_skill_group.gems[index]

    @util.CachedProperty
    @util.accumulate
    def skill_gems(self) -> List[models.Gems]:  # Added for convenience
        for group in self.skill_groups:
            for gem in group.gems:
                yield gem

    @util.CachedProperty
    def active_skill_tree(self) -> models.Tree:
        index = int(self.xml.find("Tree").get("activeSpec")) - 1
        return self.trees[index]

    @util.CachedProperty
    @util.accumulate
    def trees(self) -> List[models.Tree]:
        for spec in self.xml.find("Tree").findall("Spec"):
            url = spec.find("URL").text.strip("\n\r\t")
            sockets = {int(s.get("nodeId")): int(s.get("itemId")) for s in spec.findall("Socket")}
            yield models.Tree(url, sockets)

    @util.CachedProperty
    def notes(self) -> str:
        return self.xml.find("Notes").text.rstrip("\n\r\t")

    @util.CachedProperty
    def active_item_set(self) -> int:
        return int(self.xml.find("Items").get("activeItemSet"))

    @util.CachedProperty
    def second_weapon_set(self) -> bool:
        return True if self.xml.find("Items").get("useSecondWeaponSet") == "true" else False

    @util.CachedProperty
    @util.accumulate
    def items(self) -> List[models.Item]:
        for text in self.xml.find("Items").findall("Item"):
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
            item_text = "\n".join(util.text_parse(util.item_text(item), _variant, _mod_ranges))
            yield models.Item(rarity, name, base, shaper, elder, quality, sockets, level_req, item_level, implicit,
                              item_text)

    @util.CachedProperty
    def current_item_set(self) -> Dict[str, int]:
        return {item.get("name"): int(item.get("itemId"))
                for item in self.xml.find("Items").findall("Slot")}

    @util.CachedProperty
    def item_sets(self) -> Dict[Dict[str, int]]:
        return {slot.get("name"): int(slot.get("itemId"))
                for item_set in self.xml.findall("ItemSet") for slot in item_set.findall("Slot")}

    @util.CachedProperty
    def config(self) -> config.Config:
        def _convert_fields(item: lxml.RestrictedElement) -> Union[True, int, str]:
            if item.get("boolean"):
                return True
            elif item.get("number"):
                return int(item.get("number"))
            elif item.get("string"):
                return item.get("string").capitalize()
        kwargs = {CONFIG_MAP[i.get("name")]: _convert_fields(i) for i in self.xml.find("Config").findall("Input")}
        kwargs["character_level"] = self.level
        return config.Config(**kwargs)
