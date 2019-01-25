# Built-ins
from dataclasses import dataclass, InitVar
# Project
from pobapi.constants import MONSTER_DAMAGE_TABLE, MONSTER_LIFE_TABLE
# Third-party
from dataslots import with_slots

__all__ = ["Config"]


@dataclass
class GeneralConfig:
    """Class that holds general build configuration data.

    :param resistance_penalty: Resistance penalty obtained by slaying Kitava.
        Possible values: 0, -30, -60 (default).
    :param enemy_level: Level of enemies.
        Possible values: 1 to 100.
    :param enemy_physical_hit_damage: Damage enemies deal with physical hits.
    :param detonate_dead_corpse_life: Life of corpses consumed by Detonate Dead.
    :param is_stationary: Player is stationary.
    :param is_moving: Player is moving.
    :param is_on_full_life: Player is on full life.
    :param is_on_low_life: Player is on low life.
    :param is_on_full_energy_shield: Player is on full energy shield.
    :param has_energy_shield: Player currently has energy shield.
    :param minions_on_full_life: The player's minions are on full life.
    :param ignite_mode: Controls how ignite damage is calculated.
        Possible values: 'Average', 'Crit'"""
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
    """Class that holds skill configuration data.

    :param aspect_of_the_avian_avians_might: Whether Avian's Might is active.
    :param aspect_of_the_avian_avians_flight: Whether Avian's Flight is active.
    :param aspect_of_the_cat_cats_stealth: Whether Cat's Stealth is active.
    :param aspect_of_the_cat_cats_agility: Whether Cats's Agility is active.
    :param override_crab_barriers: Overridden number of crab barriers.
    :param aspect_of_the_spider_web_stacks: Number of web stacks on enemies.
    :param dark_pact_skeleton_life: Skeleton life points used for Dark Pact damage calculation.
    :param ice_nova_cast_on_frostbolt: Whether the player casts Ice Nova on a Frost Bolt.
    :param innervate_innervation: Whether the Innervate innervation buff is active.
    :param raise_spectres_spectre_level: Level of spectres raised by Raise Spectre.
    :param siphoning_trap_affected_enemies: Number of enemies affected by Siphoning Trap
    :param raise_spectres_enable_curses: Whether the curses of spectres are active.
    :param raise_spectres_blade_vortex_blade_count: Number of Blade Vortex stacks of spectres (provided they cast
        Blade Vortex)
    :param summon_lightning_golem_enable_wrath: Whether a Lightning Golem's wrath buff is active.
    :param vortex_cast_on_frostbolt: Whether the player casts Vortex on a Frost Bolt."""
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
    """Class that holds mapping configuration data.
    Note: Many map mods have different tiers for white, yellow and red maps; documented as tuples (white, yellow, red).

    :param enemy_physical_reduction: Whether enemies have physical damage reduction.
        Possible values: (20%, 30%, 40%).
    :param enemy_hexproof: Whether enemies are hexproof.
    :param less_curse_effect: Whether enemies have reduced effect of curses on them.
        Possible values: (25%, 40%, 60%).
    :param enemy_avoid_poison_blind_bleed: Whether enemies have a chance to avoid poison, blind and bleed.
        Possible values: (25%, 45%, 65%).
    :param enemy_resistances: Whether enemies have increased elemental and chaos resistances.
        Possible values: ((20%, 15%), (30%, 20%), (40%, 25%)):
    :param elemental_equilibrium: Whether player have Elemental Equilibrium.
    :param no_leech: Whether players cannot leech life/mana/energy shield.
    :param reduced_flask_charges: Whether players gain reduced flask charges.
        Possible values: (30%, 40%, 50%).
    :param minus_max_resists: Whether players have reduced maximum resistances.
        Possible values: (0%, 5-8%, 9-12%).
    :param less_aoe: Whether players have less area of effect.
        Possible values: (15%, 20%, 25%):
    :param enemy_avoid_status_ailment: Whether enemies have a chance to avoid status ailments.
        Possible values: (30%, 60%, 90%).
    :param enemy_increased_accuracy: Whether enemies hav increased accuracy.
        Possible values: (30%, 40%, 50%).
    :param less_armour_block: Whether players have less armour and block chance.
        Possible values: ((20%, 20%), (25%, 30%), (30%, 40%)).
    :param point_blank: Whether players have Point Blank.
    :param less_recovery: Whether players have less life/mana/energy shield recovery rate.
        Possible values: (20%, 40%, 60%).
    :param no_regen: Whether players cannot regenerate life/mana/energy shield.
    :param enemy_takes_reduced_extra_crit_damage: Whether enemies take reduced extra damage from critical strikes.
        Possible values: (25-30%, 31-35%, 36-40%).
    :param curse_assassins_mark: Level of Assassin's Mark applying to players.
    :param curse_conductivity: Level Conductivity applying to players.
    :param curse_despair: Level of Despair applying to players.
    :param curse_elemental_weakness: Level of Elemental Weakness applying to players.
    :param curse_enfeeble: Level of Enfeeble applying to players.
    :param curse_flammability: Level of Flammability applying to players.
    :param curse_frostbite: Level of Frostbite applying to players.
    :param curse_poachers_mark: Level of Poacher's Mark applying to players.
    :param curse_projectile_weakness: Level of Projectile Weakness applying to players.
    :param curse_punishment: Level of Punishment applying to players.
    :param curse_temporal_chains: Level of Temporal Chains applying to players.
    :param curse_vulnerability: Level of Vulnerability applying to players.
    :param curse_warlords_mark: Level of Warlord's Mark applying to players."""
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
    """Class that holds DPS configuration data.

    :param lucky_crits: Whether the player's hits are lucky.
    :param number_of_times_skill_has_chained: Number of times the main skill has chained.
    :param projectile_distance: Projectile travel distance.
    :param enemy_in_close_range: Whether enemies are in close range.
    :param enemy_moving: Whether enemies are moving.
    :param enemy_on_full_life: Whether enemies are on full life.
    :param enemy_on_low_life: Whether enemies are on low life.
    :param enemy_cursed: Whether enemies are cursed.
    :param enemy_bleeding: Whether enemies are bleeding.
    :param enemy_poisoned: Whether enemies are poisoned.
    :param enemy_number_of_poison_stacks: Number of poison stacks on enemies.
    :param enemy_maimed: Whether enemies are maimed.
    :param enemy_hindered: Whether enemies are hindered.
    :param enemy_blinded: Whether enemies are blinded.
    :param enemy_taunted: Whether enemies are taunted.
    :param enemy_burning: Whether enemies are burning.
    :param enemy_ignited: Whether enemies are ignited.
    :param enemy_chilled: Whether enemies are chilled.
    :param enemy_frozen: Whether enemies are frozen.
    :param enemy_shocked: Whether enemies are shocked.
    :param enemy_number_of_freeze_shock_ignite: Number of enemies frozen, shocked, or ignited recently.
    :param enemy_intimidated: Whether enemies are intimidated.
    :param enemy_covered_in_ash:  Whether enemies are covered in ash.
    :param enemy_rare_or_unique: Whether enemies are rare or unique.
    :param enemy_boss: Whether enemies are bosses.
    :param enemy_physical_damage_reduction: Enemy physical damage reduction.
    :param enemy_fire_resist: Enemy fire resistance.
    :param enemy_cold_resist: Enemy cold resistance.
    :param enemy_lightning_resist: Enemy lightning resistance.
    :param enemy_chaos_resist: Enemy chaos resistance.
    :param enemy_hit_by_fire_damage: Whether enemies were hit by fire damage.
    :param enemy_hit_by_cold_damage: Whether enemies were hit by cold damage.
    :param enemy_hit_by_lightning_damage: Whether enemies were hit by lightning damage.
    :param elemental_equilibrium_ignore_hit_damage: Whether to ignore skill hit damage resetting Elemental Equilibrium.
    """
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


@with_slots
@dataclass
class Config(GeneralConfig, SkillConfig, MapConfig, CombatConfig, DPSOptions):
    """Class that holds build configuration data.

    :param resistance_penalty: Resistance penalty obtained by slaying Kitava.
        Possible values: 0, -30, -60 (default).
    :param enemy_level: Level of enemies.
        Possible values: 1 to 100.
    :param enemy_physical_hit_damage: Damage enemies deal with physical hits.
    :param detonate_dead_corpse_life: Life of corpses consumed by Detonate Dead.
    :param is_stationary: Player is stationary.
    :param is_moving: Player is moving.
    :param is_on_full_life: Player is on full life.
    :param is_on_low_life: Player is on low life.
    :param is_on_full_energy_shield: Player is on full energy shield.
    :param has_energy_shield: Player currently has energy shield.
    :param minions_on_full_life: The player's minions are on full life.
    :param ignite_mode: Controls how ignite damage is calculated.
        Possible values: 'Average', 'Crit'
    :param aspect_of_the_avian_avians_might: Whether Avian's Might is active.
    :param aspect_of_the_avian_avians_flight: Whether Avian's Flight is active.
    :param aspect_of_the_cat_cats_stealth: Whether Cat's Stealth is active.
    :param aspect_of_the_cat_cats_agility: Whether Cats's Agility is active.
    :param override_crab_barriers: Overridden number of crab barriers.
    :param aspect_of_the_spider_web_stacks: Number of web stacks on enemies.
    :param dark_pact_skeleton_life: Skeleton life points used for Dark Pact damage calculation.
    :param ice_nova_cast_on_frostbolt: Whether the player casts Ice Nova on a Frost Bolt.
    :param innervate_innervation: Whether the Innervate innervation buff is active.
    :param raise_spectres_spectre_level: Level of spectres raised by Raise Spectre.
    :param siphoning_trap_affected_enemies: Number of enemies affected by Siphoning Trap
    :param raise_spectres_enable_curses: Whether the curses of spectres are active.
    :param raise_spectres_blade_vortex_blade_count: Number of Blade Vortex stacks of spectres (provided they cast
        Blade Vortex)
    :param summon_lightning_golem_enable_wrath: Whether a Lightning Golem's wrath buff is active.
    :param vortex_cast_on_frostbolt:Whether the player casts Vortex on a Frost Bolt.
        :param lucky_crits: Whether the player's hits are lucky.
    :param number_of_times_skill_has_chained: Number of times the main skill has chained.
    :param projectile_distance: Projectile travel distance.
    :param enemy_in_close_range: Whether enemies are in close range.
    :param enemy_moving: Whether enemies are moving.
    :param enemy_on_full_life: Whether enemies are on full life.
    :param enemy_on_low_life: Whether enemies are on low life.
    :param enemy_cursed: Whether enemies are cursed.
    :param enemy_bleeding: Whether enemies are bleeding.
    :param enemy_poisoned: Whether enemies are poisoned.
    :param enemy_number_of_poison_stacks: Number of poison stacks on enemies.
    :param enemy_maimed: Whether enemies are maimed.
    :param enemy_hindered: Whether enemies are hindered.
    :param enemy_blinded: Whether enemies are blinded.
    :param enemy_taunted: Whether enemies are taunted.
    :param enemy_burning: Whether enemies are burning.
    :param enemy_ignited: Whether enemies are ignited.
    :param enemy_chilled: Whether enemies are chilled.
    :param enemy_frozen: Whether enemies are frozen.
    :param enemy_shocked: Whether enemies are shocked.
    :param enemy_number_of_freeze_shock_ignite: Number of enemies frozen, shocked, or ignited recently.
    :param enemy_intimidated: Whether enemies are intimidated.
    :param enemy_covered_in_ash:  Whether enemies are covered in ash.
    :param enemy_rare_or_unique: Whether enemies are rare or unique.
    :param enemy_boss: Whether enemies are bosses.
    :param enemy_physical_damage_reduction: Enemy physical damage reduction.
    :param enemy_fire_resist: Enemy fire resistance.
    :param enemy_cold_resist: Enemy cold resistance.
    :param enemy_lightning_resist: Enemy lightning resistance.
    :param enemy_chaos_resist: Enemy chaos resistance.
    :param enemy_hit_by_fire_damage: Whether enemies were hit by fire damage.
    :param enemy_hit_by_cold_damage: Whether enemies were hit by cold damage.
    :param enemy_hit_by_lightning_damage: Whether enemies were hit by lightning damage.
    :param elemental_equilibrium_ignore_hit_damage: Whether to ignore skill hit damage resetting Elemental Equilibrium.
    """
    character_level: InitVar[int] = None

    def __post_init__(self, character_level: int):
        if self.enemy_level is None:
            self.enemy_level = min(character_level, 84)
        if self.enemy_physical_hit_damage is None:
            self.enemy_physical_hit_damage = MONSTER_DAMAGE_TABLE[self.enemy_level - 1] * 1.5
        if self.detonate_dead_corpse_life is None:
            self.detonate_dead_corpse_life = MONSTER_LIFE_TABLE[self.enemy_level - 1]
