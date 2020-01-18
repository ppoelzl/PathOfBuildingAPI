# Built-ins
from typing import List, Optional, Union

# Project
from pobapi import config, constants, models, stats
from pobapi.util import _get_stat, _skill_tree_nodes, _get_text
from pobapi.util import _fetch_xml_from_import_code, _fetch_xml_from_url

# Third-party
from lxml.etree import fromstring
from unstdlib.standard.functools_ import memoized_property
from unstdlib.standard.list_ import listify

"""API for PathOfBuilding's XML export format."""

__all__ = ["PathOfBuildingAPI", "from_url", "from_import_code"]


class PathOfBuildingAPI:
    """Instances of this class are single Path Of Building pastebins.

    :param xml: Path of Building XML document in byte format.

    .. note:: XML must me in byte format, not string format.
        This is required because the XML contains encoding information.

    .. note:: To instantiate from pastebin.com links or import codes, use
        :func:`~pobapi.api.from_url` or
        :func:`~pobapi.api.from_import_code`, respectively."""

    def __init__(self, xml: bytes):
        self.xml = fromstring(xml)

    @memoized_property
    def class_name(self) -> str:
        """Get a character's class.

        :return: Character class.
        :rtype: :class:`str`"""
        return self.xml.find("Build").get("className")

    @memoized_property
    def ascendancy_name(self) -> Optional[str]:
        """Get a character's ascendancy class.

        :return: Character ascendancy class, if ascended.
        :rtype: :data:`~typing.Optional`\\[:class:`str`]"""
        return self.xml.find("Build").get("ascendClassName")

    @memoized_property
    def level(self) -> int:
        """Get a character's level.

        :return: Character level.
        :rtype: :class:`int`"""
        return int(self.xml.find("Build").get("level"))

    @memoized_property
    def bandit(self) -> Optional[str]:
        """Get a character's bandit choice.

        :return: Character bandit choice.
        :rtype: :data:`~typing.Optional`\\[:class:`str`]"""
        return self.xml.find("Build").get("bandit")

    @memoized_property
    def active_skill_group(self) -> models.SkillGroup:
        """Get a character's main skill setup.

        :return: Main skill setup.
        :rtype: :class:`~pobapi.models.SkillGroup`"""
        index = int(self.xml.find("Build").get("mainSocketGroup")) - 1
        return self.skill_groups[index]

    @memoized_property
    def stats(self) -> stats.Stats:
        """Namespace for character stats.

        :return: Character stats.
        :rtype: :class:`~pobapi.stats.Stats`"""
        kwargs = {
            constants.STATS_MAP.get(i.get("stat")): float(i.get("value"))
            for i in self.xml.find("Build").findall("PlayerStat")
        }
        return stats.Stats(**kwargs)

    @memoized_property
    @listify
    def skill_groups(self) -> List[models.SkillGroup]:
        """Get a character's skill setups.

        :return: Skill setups.
        :rtype: :class:`~typing.List`\\[:class:`~pobapi.models.SkillGroup`]"""
        for skill in self.xml.find("Skills").findall("Skill"):
            enabled = True if skill.get("enabled") == "true" else False
            label = skill.get("label")
            active = (
                int(skill.get("mainActiveSkill"))
                if not skill.get("mainActiveSkill") == "nil"
                else None
            )
            abilities = self._abilities(skill)
            yield models.SkillGroup(enabled, label, active, abilities)

    @memoized_property
    def active_skill(self) -> Union[models.Gem, models.GrantedAbility]:
        """Get a character's main skill.

        :return: Main skill.
        :rtype: :data:`~typing.Union`\\[:class:`~pobapi.models.Gem`,
            :class:`~pobapi.models.GrantedAbility`]"""
        index = self.active_skill_group.active - 1
        # Short-circuited for the most common case
        if not index:
            return self.active_skill_group.abilities[index]
        # For base skills on Vaal skill gems,
        # the offset is as if the base skill gems would also be present.
        # Simulating this is easier than calculating the adjusted offset.
        active = [gem for gem in self.active_skill_group.abilities if not gem.support]
        duplicate = []
        for gem in active:
            if gem.name.startswith("Vaal"):
                duplicate.append(gem)
            duplicate.append(gem)
        if len(duplicate) > 1 and duplicate[index] == duplicate[index - 1]:
            gem = duplicate[index - 1]
            name = constants.VAAL_SKILL_MAP.get(
                gem.name, gem.name.rpartition("Vaal ")[2]
            )
            return models.Gem(name, gem.enabled, gem.quality, gem.level, gem.support)
        return self.active_skill_group.abilities[index]

    @memoized_property
    @listify
    def skill_gems(self) -> List[models.Gem]:  # Added for convenience
        """Get a list of all skill gems on a character.

        .. note: Excludes abilities granted by items.

        :return: Skill gems.
        :rtype: :class:`~typing.List`\\[:class:`~pobapi.models.Gem`]"""

        for skill in self.xml.find("Skills").findall("SkillGroup"):
            if not skill.get("source"):
                yield from self._abilities(skill)

    @memoized_property
    def active_skill_tree(self) -> models.Tree:
        """Get a character's current skill tree.

        :return: Skill tree.
        :rtype: :class:`~pobapi.models.Tree`"""
        index = int(self.xml.find("Tree").get("activeSpec")) - 1
        return self.trees[index]

    @memoized_property
    @listify
    def trees(self) -> List[models.Tree]:
        """Get a list of all skill trees of a character.

        :return: Skill trees.
        :rtype: :class:`~typing.List`\\[:class:`~pobapi.models.Tree`]"""
        for spec in self.xml.find("Tree").findall("Spec"):
            url = spec.find("URL").text.strip("\n\r\t")
            nodes = _skill_tree_nodes(url)
            sockets = {
                int(s.get("nodeId")): int(s.get("itemId"))
                for s in spec.findall("Socket")
            }
            yield models.Tree(url, nodes, sockets)

    @memoized_property
    def keystones(self) -> models.Keystones:
        """Namespace for a character's keystones.

        Iterate over the keystones property to only get active keystones.

        :return: Keystones.
        :rtype: :class:`~pobapi.models.Keystones`"""
        kwargs = {
            keystone: True if id_ in self.active_skill_tree.nodes else False
            for keystone, id_ in constants.KEYSTONE_IDS.items()
        }
        return models.Keystones(**kwargs)

    @memoized_property
    def notes(self) -> str:
        """Get notes of a build's author.

        :return: Build notes.
        :rtype: :class:`str`"""
        return self.xml.find("Notes").text.strip("\n\r\t").rstrip("\n\r\t")

    @memoized_property
    def second_weapon_set(self) -> bool:
        """Get whether a character primarily uses their second weapon set.

        :return: Truth value.
        :rtype: :class:`bool`"""
        return (
            True
            if self.xml.find("Items").get("useSecondWeaponSet") == "true"
            else False
        )

    @memoized_property
    @listify
    def items(self) -> List[models.Item]:
        """Get a list of all items of a Path Of Building build.
        
        :return: Items.
        :rtype: :class:`~typing.List`\\[:class:`~pobapi.models.Item`]"""
        for text in self.xml.find("Items").findall("Item"):
            variant = text.get("variant")
            alt_variant = text.get("variantAlt")
            # "variantAlt" is for the second Watcher's Eye unique mod.
            # The 3-stat variant obtained from Uber Elder is not yet implemented in PoB.
            mod_ranges = [float(i.get("range")) for i in text.findall("ModRange")]
            item = text.text.strip("\n\r\t").splitlines()
            rarity = _get_stat(item, "Rarity: ").capitalize()
            name = item[1]
            base = name if rarity in ("Normal", "Magic") else item[2]
            uid = _get_stat(item, "Unique ID: ")
            shaper = True if _get_stat(item, "Shaper Item") else False
            elder = True if _get_stat(item, "Elder Item") else False
            crafted = True if _get_stat(item, "{crafted}") else False
            _quality = _get_stat(item, "Quality: ")
            quality = int(_quality) if _quality else None
            _sockets = _get_stat(item, "Sockets: ")
            sockets = (
                tuple(tuple(group.split("-")) for group in _sockets.split())
                if _sockets
                else None
            )
            level_req = int(_get_stat(item, "LevelReq: ") or 1)
            item_level = int(_get_stat(item, "Item Level: ") or 1)
            implicit = int(_get_stat(item, "Implicits: "))
            item_text = _get_text(item, variant, alt_variant, mod_ranges)
            # fmt: off
            yield models.Item(rarity, name, base, uid, shaper, elder, crafted, quality,
                              sockets, level_req, item_level, implicit, item_text)
            # fmt: on

    @memoized_property
    def active_item_set(self) -> models.Set:
        """Get the item set a character is currently wearing.

        :return: Item set.
        :rtype: :class:`~pobapi.models.Set`"""
        index = int(self.xml.find("Items").get("activeItemSet")) - 1
        return self.item_sets[index]

    @memoized_property
    @listify
    def item_sets(self) -> List[models.Set]:
        """Get a list of all item sets of a character.

        :return: Item sets.
        :rtype: :class:`~typing.List`\\[:class:`~pobapi.models.Set`]"""
        for item_set in self.xml.find("Items").findall("ItemSet"):
            kwargs = {
                constants.SET_MAP.get(slot.get("name")): int(slot.get("itemId"))
                if not slot.get("itemId") == "0"
                else None
                for slot in item_set.findall("Slot")
            }
            yield models.Set(**kwargs)

    @memoized_property
    def config(self) -> config.Config:
        """Namespace for Path Of Building config tab's options and values.

        :return: Path Of Building config.
        :rtype: :class:`~pobapi.config.Config`"""

        def _convert_fields(item):
            if item.get("boolean"):
                return True
            elif item.get("number"):
                return int(item.get("number"))
            elif item.get("string"):
                return item.get("string").capitalize()

        kwargs = {
            constants.CONFIG_MAP.get(i.get("name")): _convert_fields(i)
            for i in self.xml.find("Config").findall("Input")
        }
        kwargs["character_level"] = self.level
        return config.Config(**kwargs)

    @classmethod
    @listify
    def _abilities(cls, skill) -> List[Union[models.Gem, models.GrantedAbility]]:
        """Get a list of abilities, whether they are granted by gems or by items.

        :return: Abilities.
        :rtype: :class:`~typing.List`\\
            [:data:`~typing.Union`\\[:class:`~pobapi.models.Gem`,
            :class:`~pobapi.models.GrantedAbility`]]"""
        for ability in skill:
            gem_id = ability.get("gemId")
            name = ability.get("nameSpec")
            enabled = True if ability.get("enabled") == "true" else False
            level = int(ability.get("level"))
            if gem_id:
                quality = int(ability.get("quality"))
                support = (
                    True if ability.get("skillId").startswith("Support") else False
                )
                yield models.Gem(name, enabled, level, quality, support)
            else:
                name = name or constants.SKILL_MAP.get(ability.get("skillId"))
                yield models.GrantedAbility(name, enabled, level)


def from_url(url: str, timeout: float = 6.0) -> PathOfBuildingAPI:
    """Instantiate build class from a pastebin.com link generated with Path Of Building.

    :raises: :class:`~requests.URLRequired`, :class:`~requests.Timeout`,
        :class:`~requests.ConnectionError`, :class:`~requests.HTTPError`,
        :class:`~requests.TooManyRedirects`, :class:`~requests.RequestException`

    :param url: pastebin.com link generated with Path Of Building.
    :param timeout: Timeout for the request."""
    return PathOfBuildingAPI(_fetch_xml_from_url(url, timeout))


def from_import_code(import_code: str) -> PathOfBuildingAPI:
    """Instantiate build class from an import code generated with Path Of Building.

    :raises: :class:`TypeError`, :class:`ValueError`

    :param import_code: import code generated with Path Of Building."""
    return PathOfBuildingAPI(_fetch_xml_from_import_code(import_code))
