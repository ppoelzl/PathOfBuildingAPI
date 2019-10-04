# Built-ins
from dataclasses import dataclass, field, InitVar
from typing import Union

# Project
from pobapi.constants import MONSTER_DAMAGE_TABLE, MONSTER_LIFE_TABLE

# Third-party
from dataslots import with_slots

__all__ = ["Config"]


@with_slots
@dataclass
class Config:
    """Config(*args)
    Class that holds build configuration data.

    .. note:: Many map mods have different tiers for white, yellow and red maps;
        documented as tuples (white, yellow, red).

    :param resistance_penalty: Resistance penalty obtained by slaying Kitava.
        Possible values: 0, -30, -60 (default).
    :param enemy_level: Level of enemies.
        Possible values: 1 to 100.
    :param enemy_physical_hit_damage: Damage enemies deal with physical hits.
    :param detonate_dead_corpse_life: Life of corpses consumed by Detonate Dead.
    :param is_stationary: Whether the player is stationary.
    :param is_moving: Whether the player is moving.
    :param is_on_full_life: Whether the player is on Full Life.
    :param is_on_low_life: Whether the player is on Low Life.
    :param is_on_full_energy_shield: Whether the player is on Full Energy Shield.
    :param has_energy_shield: Whether the player currently has energy shield.
    :param minions_on_full_life: Whether the player's minions are on Full Life.
    :param ignite_mode: Controls how ignite damage is calculated.
        Possible values: ('Average', 'Crit').
    :param aspect_of_the_avian_avians_might: Whether Avian's Might is active.
    :param aspect_of_the_avian_avians_flight: Whether Avian's Flight is active.
    :param aspect_of_the_cat_cats_stealth: Whether Cat's Stealth is active.
    :param aspect_of_the_cat_cats_agility: Whether Cats's Agility is active.
    :param override_crab_barriers: Overridden number of crab barriers.
    :param aspect_of_the_spider_web_stacks: Number of web stacks on enemies.
    :param banner_planted: Whether the player has planted a banner.
    :param banner_stages: Number of banner stages.
    :param in_bloodstorm: Whether the player is in a Bloodstorm.
    :param in_sandstorm: Whether the player is in a Sandstorm.
    :param brand_attached: Whether the player has a brand attached.
    :param dark_pact_skeleton_life: Skeleton life points used for Dark Pact damage calculation.
    :param deathmark: Whether the player applies Deathmark.
    :param herald_of_agony_stacks: Number of Virulence stacks on Herald of Agony.
    :param ice_nova_cast_on_frostbolt: Whether the player casts Ice Nova on a Frost Bolt.
    :param infusion: Whether the Infusion Infusion buff is active.
    :param innervate_innervation: Whether the Innervate Innervation buff is active.
    :param intensify_stacks: Number of Intensify stacks.
    :param meat_shield_enemy_nearby: Whether there are enemies near your minions supported by Meat Shield Support.
    :param raise_spectres_spectre_level: Level of spectres raised by Raise Spectre.
    :param raise_spectres_enable_curses: Whether the curses of spectres are active.
    :param raise_spectres_blade_vortex_blade_count: Number of Blade Vortex stacks of spectres.
    :param raise_spectres_kaom_fire_beam_totem_stage: Number of fire beam stages of spectres.
    :param raise_spectres_enable_summoned_ursa_rallying_cry: Whether the Rallying Cry of ursa spectres is active.
    :param raise_spiders_spider_count: Number of spiders from Raise Spiders.
    :param siphoning_trap_affected_enemies: Number of enemies affected by Siphoning Trap.
    :param stance: Controls whether the player is in Blood Stance or Sand Stance.
        Possible values: ('Blood', 'Sand').
    :param summon_holy_relic_enable_holy_relic_buff: Whether the Holy Relic buff of Summon Holy Relics is active.
    :param summon_lightning_golem_enable_wrath: Whether a Lightning Golem's wrath buff is active.
    :param vortex_cast_on_frostbolt: Whether the player casts Vortex on a Frost Bolt.
    :param wave_of_conviction_exposure_type: Controls which Exposure damage type is selected.
        Possible values: ('Fire', 'Cold', 'Lightning').
    :param winter_orb_stages: Number of stages of Winter Orb.
    :param enemy_physical_reduction: Whether enemies have physical damage reduction.
        Possible values: (20%, 30%, 40%).
    :param enemy_hexproof: Whether enemies are hexproof.
    :param less_curse_effect: Whether enemies have reduced effect of curses on them.
        Possible values: (25%, 40%, 60%).
    :param enemy_avoid_poison_blind_bleed: Whether enemies have a chance to avoid poison, blind and bleed.
        Possible values: (25%, 45%, 65%).
    :param enemy_resistances: Whether enemies have increased elemental and chaos resistances.
        Possible values: ((20%, 15%), (30%, 20%), (40%, 25%)).
    :param elemental_equilibrium: Whether player have Elemental Equilibrium.
    :param no_leech: Whether players cannot leech life/mana/energy shield.
    :param reduced_flask_charges: Whether players gain reduced flask charges.
        Possible values: (30%, 40%, 50%).
    :param minus_max_resists: Whether players have reduced maximum resistances.
        Possible values: (0%, 5-8%, 9-12%).
    :param less_aoe: Whether players have less area of effect.
        Possible values: (15%, 20%, 25%).
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
    :param curse_warlords_mark: Level of Warlord's Mark applying to players.
    :param use_power_charges: Whether the player uses power charges.
    :param max_power_charges: Whether the player is at maximum power charges.
    :param use_frenzy_charges: Whether the player uses frenzy charges.
    :param max_frenzy_charges: Whether the player is at maximum frenzy charges.
    :param use_endurance_charges: Whether the player uses endurance charges.
    :param max_endurance_charges: Whether the player is at maximum endurance charges.
    :param use_siphoning_charges: Whether the player uses siphoning charges.
    :param use_challenger_charges: Whether the player uses Challenger Charges.
    :param max_challenger_charges: Whether the player is at maximum Challenger Charges.
    :param use_blitz_charges: Whether the player uses Blitz Charges.
    :param max_blitz_charges: Whether the player is at maximum Blitz Charges.
    :param use_inspiration_charges: Whether the player uses Inspiration Charges.
    :param max_inspiration_charges: Whether the player is at maximum Inspiration Charges.
    :param max_siphoning_charges: Whether the player is at maximum siphoning charges.
    :param minions_use_power_charges: Whether the player's minions use power charges.
    :param minions_use_frenzy_charges: Whether the player's minions use frenzy charges.
    :param minions_use_endurance_charges: Whether the player's minions use endurance charges.
    :param focus: Whether the player has Focus.
    :param onslaught: Whether the player has Onslaught.
    :param unholy_might: Whether the player has Unholy Might.
    :param phasing: Whether the player has Phasing.
    :param fortify: Whether the player has Fortify.
    :param tailwind: Whether the player has Tailwind.
    :param adrenaline: Whether the player has Adrenaline.
    :param divinity: Whether the player has Divinity.
    :param rage: Whether the player has Rage.
    :param leeching: Whether the player is leeching.
    :param leeching_life: Whether the player is leeching Life.
    :param leeching_energy_shield: Whether the player is leeching Energy Shield.
    :param leeching_mana: Whether the player is leeching Mana.
    :param using_flask: Whether the player is using a flask.
    :param has_totem: Whether the player has a totem.
    :param number_of_nearby_allies: Number of nearby allies.
    :param number_of_nearby_enemies: Number of nearby enemies.
    :param number_of_nearby_corpses: Number of nearby corpses.
    :param on_consecrated_ground: Whether the player is on consecrated ground.
    :param on_burning_ground: Whether the player is on burning ground.
    :param on_chilled_ground: Whether the player is on chilled ground.
    :param on_shocked_ground: Whether the player is on shocked ground.
    :param burning: Whether the player is burning.
    :param ignited: Whether the player is ignited.
    :param chilled: Whether the player is chilled.
    :param frozen: Whether the player is frozen.
    :param shocked: Whether the player is shocked.
    :param bleeding: Whether the player is bleeding.
    :param poisoned: Whether the player is poisoned.
    :param number_of_poison_stacks: Number of poison stacks on the player.
    :param only_one_nearby_enemy: Whether there is only one enemy nearby.
    :param hit_recently: Whether the player has hit recently.
    :param crit_recently: Whether the player has crit recently.
    :param skill_crit_recently: Whether one the player's skills has crit recently.
    :param non_crit_recently: Whether the player has not crit recently.
    :param killed_recently: Whether the player has killed recently.
    :param number_of_enemies_killed_recently: Number of enemies killed by the player recently.
    :param totems_killed_recently: Whether the player's totems killed recently.
    :param number_of_totems_killed_recently: Number of enemies killed by the player's totems recently.
    :param minions_killed_recently: Whether the player's minions killed recently.
    :param number_of_minions_killed_recently: Number of enemies killed by the player's minions recently.
    :param killed_affected_by_dot: Whether the player has killed an enemy affected by damage over time recently.
    :param number_of_shocked_enemies_killed_recently: Number of shocked enemies killed by the player recently.
    :param frozen_enemy_recently: Whether the player has frozen an enemy recently.
    :param shattered_enemy_recently: Whether the player has shattered an enemy recently.
    :param ignited_enemy_recently: Whether the player has ignited an enemy recently.
    :param shocked_enemy_recently: Whether the player has shocked an enemy recently.
    :param number_of_poisons_applied_recently: Number of poisons applied by the player recently.
    :param been_hit_recently: Whether the player has been hit recently.
    :param been_crit_recently: Whether the player has been crit recently.
    :param been_savage_hit_recently: Whether the player has been savage hit recently.
    :param hit_by_fire_damage_recently: Whether the player has been hit by fire damage recently.
    :param hit_by_cold_damage_recently: Whether the player has been hit by cold damage recently.
    :param hit_by_lightning_damage_recently: Whether the player has been hit by lightning damage recently.
    :param blocked_recently: Whether the player has blocked recently.
    :param blocked_attack_recently: Whether the player has blocked an attack recently.
    :param blocked_spell_recently: Whether the player has blocked a spell recently.
    :param energy_shield_recharge_started_recently: Whether the player's energy shield recharge started recently.
    :param pendulum_of_destruction: Controls Pendulum of Destruction mode.
        Possible values: ('Area', 'Damage').
    :param elemental_conflux: Controls Elemental Conflux mode.
        Possible values: ('Chilling', 'Shocking', 'Igniting', 'All').
    :param bastion_of_hope: Whether the player has Bastion of Hope.
    :param her_embrace: Whether the player is in Her Embrace.
    :param used_skill_recently: Whether the player has used a skill recently.
    :param attacked_recently: Whether the player has attacked recently.
    :param cast_spell_recently: Whether the player has cast a spell recently.
    :param used_fire_skill_recently: Whether the player has used a fire skill recently.
    :param used_cold_skill_recently: Whether the player has used a cold skill recently.
    :param used_minion_skill_recently: Whether the player has used a minion skill recently.
    :param used_movement_skill_recently: Whether the player has used a movement skill recently.
    :param used_vaal_skill_recently: Whether the player has used a vaal skill recently.
    :param used_warcry_recently: Whether the player has used a warcry recently.
    :param number_of_mines_detonated_recently: Number of mines detonated recently.
    :param number_of_traps_triggered_recently: Number of traps triggered recently.
    :param consumed_corpses_recently: Whether the player has consumed corpses recently.
    :param number_of_corpses_consumed_recently: Number of corpses consumed by the player recently.
    :param taunted_enemy_recently: Whether the player has taunted an enemy recently.
    :param blocked_hit_from_unique_enemy_in_past_ten_seconds:
        Whether the player has blocked a hit from an unique enemy in the past ten seconds.
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
    :param enemy_unnerved: Whether enemies are unnerved.
    :param enemy_covered_in_ash:  Whether enemies are covered in ash.
    :param enemy_rare_or_unique: Whether enemies are rare or unique.
    :param enemy_boss: Whether enemies are bosses.
        Possible Values: (False, True, 'Shaper').
    :param enemy_physical_damage_reduction: Enemy physical damage reduction.
    :param enemy_fire_resist: Enemy fire resistance.
    :param enemy_cold_resist: Enemy cold resistance.
    :param enemy_lightning_resist: Enemy lightning resistance.
    :param enemy_chaos_resist: Enemy chaos resistance.
    :param enemy_hit_by_fire_damage: Whether enemies were hit by fire damage.
    :param enemy_hit_by_cold_damage: Whether enemies were hit by cold damage.
    :param enemy_hit_by_lightning_damage: Whether enemies were hit by lightning damage.
    :param elemental_equilibrium_ignore_hit_damage: Whether to ignore skill hit damage resetting Elemental Equilibrium.
    :param character_level: Overridden character/enemy level used to estimate hit and evasion chances, enemy life and
        damage."""

    # General Build Configuration
    resistance_penalty: int = -60
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
    ignite_mode: str = None
    # Skill Configuration
    aspect_of_the_avian_avians_might: bool = False
    aspect_of_the_avian_avians_flight: bool = False
    aspect_of_the_cat_cats_stealth: bool = False
    aspect_of_the_cat_cats_agility: bool = False
    override_crab_barriers: int = None
    aspect_of_the_spider_web_stacks: int = None
    banner_planted: bool = False
    banner_stages: int = None
    in_bloodstorm: bool = False
    in_sandstorm: bool = False
    brand_attached: bool = False
    dark_pact_skeleton_life: int = None
    deathmark: bool = False
    feeding_frenzy: bool = False
    herald_of_agony_stacks: int = None
    ice_nova_cast_on_frostbolt: bool = False
    infusion: bool = False
    innervate_innervation: bool = False
    intensify_stacks: int = None
    meat_shield_enemy_nearby: bool = False
    raise_spectres_spectre_level: int = None
    raise_spectres_enable_curses: bool = False
    raise_spectres_blade_vortex_blade_count: int = None
    raise_spectres_kaom_fire_beam_totem_stage: int = None
    raise_spectres_enable_summoned_ursa_rallying_cry: bool = False
    raise_spiders_spider_count: int = None
    siphoning_trap_affected_enemies: int = None
    stance: str = None
    summon_holy_relic_enable_holy_relic_buff: bool = False
    summon_lightning_golem_enable_wrath: bool = False
    vortex_cast_on_frostbolt: bool = False
    wave_of_conviction_exposure_type: str = None
    winter_orb_stages: int = None
    # Map Configuration
    enemy_physical_reduction: int = None
    enemy_hexproof: bool = False
    less_curse_effect: int = None
    enemy_avoid_poison_blind_bleed: int = None
    enemy_resistances: str = None
    elemental_equilibrium: bool = False
    no_leech: bool = False
    reduced_flask_charges: int = None
    minus_max_resists: int = None
    less_aoe: int = None
    enemy_avoid_status_ailment: int = None
    enemy_increased_accuracy: int = None
    less_armour_block: str = None
    point_blank: bool = False
    less_recovery: int = None
    no_regen: bool = False
    enemy_takes_reduced_extra_crit_damage: int = None
    curse_assassins_mark: int = None
    curse_conductivity: int = None
    curse_despair: int = None
    curse_elemental_weakness: int = None
    curse_enfeeble: int = None
    curse_flammability: int = None
    curse_frostbite: int = None
    curse_poachers_mark: int = None
    curse_projectile_weakness: int = None
    curse_punishment: int = None
    curse_temporal_chains: int = None
    curse_vulnerability: int = None
    curse_warlords_mark: int = None
    # Combat Configuration
    use_power_charges: bool = False
    max_power_charges: int = None
    use_frenzy_charges: bool = False
    max_frenzy_charges: int = None
    use_endurance_charges: bool = False
    max_endurance_charges: int = None
    use_siphoning_charges: bool = False
    max_siphoning_charges: int = None
    use_challenger_charges: bool = False
    max_challenger_charges: int = None
    use_blitz_charges: bool = False
    max_blitz_charges: int = None
    use_inspiration_charges: bool = False
    max_inspiration_charges: int = None
    minions_use_power_charges: bool = False
    minions_use_frenzy_charges: bool = False
    minions_use_endurance_charges: bool = False
    focus: bool = False
    onslaught: bool = False
    unholy_might: bool = False
    phasing: bool = False
    fortify: bool = False
    tailwind: bool = False
    adrenaline: bool = False
    divinity: bool = False
    rage: bool = False
    leeching: bool = False
    leeching_life: bool = False
    leeching_energy_shield: bool = False
    leeching_mana: bool = False
    using_flask: bool = False
    has_totem: bool = False
    number_of_nearby_allies: int = None
    number_of_nearby_enemies: int = None
    number_of_nearby_corpses: int = None
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
    skill_crit_recently: bool = False
    non_crit_recently: bool = False
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
    pendulum_of_destruction: str = False
    elemental_conflux: str = False
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
    # DPS Configuration
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
    enemy_unnerved: bool = False
    enemy_covered_in_ash: bool = False
    enemy_rare_or_unique: bool = False
    enemy_boss: Union[bool, str] = False
    enemy_physical_damage_reduction: int = None
    enemy_fire_resist: int = None
    enemy_cold_resist: int = None
    enemy_lightning_resist: int = None
    enemy_chaos_resist: int = None
    enemy_hit_by_fire_damage: bool = False
    enemy_hit_by_cold_damage: bool = False
    enemy_hit_by_lightning_damage: bool = False
    elemental_equilibrium_ignore_hit_damage: bool = False
    # The fields in the post init method are the only values in Path of Building's configuration tab that are
    # calculated, but can also be overridden so we potentially have to initialise them at a later point in time.
    character_level: InitVar[int] = None

    # TODO: Raise Spectre level calc on 3.0.0+
    def __post_init__(self, character_level: int):
        if character_level is None:
            character_level = 84
        if self.enemy_level is None:
            self.enemy_level = min(character_level, 84)
        if self.enemy_physical_hit_damage is None:
            self.enemy_physical_hit_damage = (
                MONSTER_DAMAGE_TABLE[self.enemy_level - 1] * 1.5
            )
        if self.detonate_dead_corpse_life is None:
            self.detonate_dead_corpse_life = MONSTER_LIFE_TABLE[self.enemy_level - 1]
