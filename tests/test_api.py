# Project
from pobapi import api
from pobapi import util
from pobapi.constants import CLASS_NAMES, ASCENDANCY_NAMES, BANDITS
# Third-Party
import pytest


@pytest.fixture(scope="module")
def build():
    with open("../resources/import_code.txt") as f:
        code = f.read()
    soup = util.fetch_import_code(code)
    return api.PathOfBuildingAPI(soup)


def test_class_name(build):
    assert build.class_name in CLASS_NAMES


def test_ascendancy_name(build):
    assert build.ascendancy_name in ASCENDANCY_NAMES or None


def test_level(build):
    assert 1 <= build.level <= 100


def test_bandit(build):
    assert build.bandit in BANDITS or None


def test_notes(build):
    assert isinstance(build.notes, str)
    assert build.notes.endswith("\n\r\t") is False


def test_second_weapon_set(build):
    assert isinstance(build.second_weapon_set, bool)


def test_stats(build):
    assert isinstance(build.stats, api.Stats)
    assert 1 <= build.stats.life
    assert 0 <= build.stats.mana


def test_config(build):
    assert isinstance(build.config, api.Config)
    assert build.config.enemy_boss in (False, True, "Shaper")


def test_item_sets(build):
    pass


def test_current_item_set(build):
    pass


def test_current_item_set_index(build):
    pass


def test_active_skill_group(build):
    pass


def test_active_skill(build):
    pass


def test_trees(build):
    for i in build.trees:
        assert isinstance(i, api.Tree)
        assert isinstance(i.url, str)
        assert isinstance(i.sockets, dict)
    assert isinstance(build.active_skill_tree, api.Tree)


def test_skill_groups(build):
    for i in build.skill_groups:
        assert isinstance(i, api.Skill)
        assert isinstance(i.enabled, bool)
        assert isinstance(i.label, str)
        assert isinstance(i.active, (int, type(None)))
        assert isinstance(i.gems, list)
        for j in i.gems:
            assert isinstance(j, api.Gems)
            assert isinstance(j.name, str)
            assert isinstance(j.enabled, bool)
            assert isinstance(j.level, int)
            assert isinstance(j.quality, int)
    assert build.skill_groups[1]  # test indexing
    # assert build.main_skill_group == build().skill_groups[0]  could use data classes for this
    assert isinstance(build.active_skill_group, api.Skill)
    assert isinstance(build.active_skill, api.Gems)


def test_items(build):
    for i in build.items:
        assert isinstance(i, api.Item)
        assert isinstance(i.rarity, str)
        assert isinstance(i.name, str)
        assert isinstance(i.base, str)
        assert isinstance(i.shaper, bool)
        assert isinstance(i.elder, bool)
        assert isinstance(i.quality, (int, type(None)))
        assert isinstance(i.sockets, (tuple, type(None)))
        assert isinstance(i.level_req, int)
        assert isinstance(i.item_level, int)
        assert isinstance(i.implicit, (int, type(None)))
        assert isinstance(i.text, str)
