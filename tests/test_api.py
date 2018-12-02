import pytest
from pobapi import api
import util
from constants import CLASS_NAMES, ASCENDANCY_NAMES, BANDITS


@pytest.fixture(scope="module")
def build():
    with open("../resources/import_code.txt") as f:
        code = f.read()
    soup = util.fetch_xml(code)
    print(type(api.PathOfBuildingAPI(soup)))
    return api.PathOfBuildingAPI(soup)


def test_class_name():
    assert build().class_name in CLASS_NAMES


def test_ascendancy_name():
    assert build().ascendancy_name in ASCENDANCY_NAMES


def test_level():
    assert 1 <= build().level <= 100


def test_bandit():
    assert build().bandit in BANDITS or None


def test_notes():
    assert isinstance(build().notes, str)
    assert build().notes.endswith("\n\r\t") is False


def test_stats():
    assert isinstance(build().stats, api.Stats)
    assert 1 <= build().stats.life
    assert 0 <= build().stats.mana


def test_config():
    assert isinstance(build().config, api.Config)
    assert build().config.enemy_boss in (False, True, "Shaper")


def test_trees():
    for i in build().trees:
        assert isinstance(i, api.Tree)
        assert isinstance(i.url, str)
        assert isinstance(i.sockets, dict)
    assert isinstance(build().active_skill_tree, api.Tree)


def test_skill_groups():
    for i in build().skill_groups:
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
    assert build().skill_groups[1]  # test indexing
    # assert build().main_skill_group == build().skill_groups[0]  could use data classes for this
    assert isinstance(build().active_skill_group, api.Skill)
    assert isinstance(build().active_skill, api.Gems)


def test_items():
    pass
