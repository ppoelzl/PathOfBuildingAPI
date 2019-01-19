# Built-ins
from dataclasses import dataclass
# Third-party
from dataslots import with_slots

__all__ = ["Stats"]


@with_slots
@dataclass
class Stats:
    """Class that holds character stat-sheet data.

    :param average_hit: Average hit damage.
    :param average_damage: Average hit damage after accuracy check.
    :param cast_speed: Spell cast speed.
    :param attack_speed: Attack speed.
    :param trap_throwing_speed: Trap throwing speed.
    :param trap_cooldown: Trap throwing cooldown.
    :param mine_laying_speed: Mine laying speed
    :param totem_placement_speed: Totem placement speed.
    :param pre_effective_crit_chance: Crit chance as displayed in-game (doesn't factor in accuracy and luck)
    :param crit_chance: Effective crit chance, factors in accuracy and luck
    :param crit_multiplier: Critical strike multiplier.
    :param hit_chance: Chance to hit with attacks.
    :param total_dps: Total Damage per second.
    :param total_dot: Total damage over time (per second)
    :param bleed_dps: Bleeding damage per second.
    :param ignite_dps: Ignite damage per second.
    :param ignite_damage: Ignite hit damage.
    :param total_dps_with_ignite: Total damage per second including ignite damage.
    :param average_damage_with_ignite: Average hit damage including ignite.
    :param poison_dps: Poison damage per second.
    :param poison_damage: Poison hit damage.
    :param total_dps_with_poison: Total damage per second including poison damage.
    :param average_damage_with_poison: Average hit damage including poison.
    :param decay_dps: Decay damage per second.
    :param skill_cooldown: Skill coodown time.
    :param area_of_effect_radius: Area of effect radius.
    :param mana_cost: Mana cost of skill.
    :param strength: Strength attribute.
    :param strength_required: Required strength.
    :param dexterity: Dexterity attribute.
    :param dexterity_required: Required dexterity.
    :param intelligence: Intelligence attribute.
    :param intelligence_required: Intelligence required.
    :param life: Life points.
    :param life_increased: Percent increased life.
    :param life_unreserved: Unreserved life points.
    :param life_unreserved_percent: Percent unreserved life.
    :param life_regen: Flat life regeneration.
    :param life_leech_rate_per_hit: Percent life leeched per hit.
    :param life_leech_gain_per_hit: Flat life leeched per hit.
    :param mana: Mana points.
    :param mana_increased: Percent increased mana.
    :param mana_unreserved: Unreserved mana points.
    :param mana_unreserved_percent: Percent unreserved mana.
    :param mana_regen: Flat mana regeneration.
    :param mana_leech_rate_per_hit: Percent mana leeched per hit.
    :param mana_leech_gain_per_hit: Flat mana leeched per hit.
    :param total_degen: Total life degeneration.
    :param net_life_regen: Net life regeneration.
    :param net_mana_regen: Net mana regeneration.
    :param energy_shield: Energy shield.
    :param energy_shield_increased: Percent increased energy shield.
    :param energy_shield_regen: Flat energy shield regeneration.
    :param energy_shield_leech_rate_per_hit: Percent energy shield leeched per hit.
    :param energy_shield_leech_gain_per_hit: Flat energy shield leeched per hit.
    :param evasion: Evasion rating.
    :param evasion_increased: Percent increased evasion rating.
    :param melee_evade_chance: Chance to evade melee attacks.
    :param projectile_evade_chance: Chance to evade projectiles.
    :param armour: Armour.
    :param armour_increased: Percent increased armour.
    :param physical_damage_reduction: Physical damage reduction.
    :param effective_movement_speed_modifier: Effective movement speed modifier.
    :param block_chance: Chance to block attacks.
    :param spell_block_chance: Chance to block spells.
    :param attack_dodge_chance: Chance to dodge attacks.
    :param spell_dodge_chance: Chance to dodge spells.
    :param fire_resistance: Fire resistance.
    :param cold_resistance: Cold resistance.
    :param lightning_resistance: Lightning resistance.
    :param chaos_resistance: Chaos resistance.
    :param fire_resistance_over_cap: Overcapped fire resistance.
    :param cold_resistance_over_cap: Overcapped cold resistance
    :param lightning_resistance_over_cap: Overcapped lightning resistance.
    :param chaos_resistance_over_cap: Overcapped chaos resistance.
    :param power_charges: Power charges.
    :param power_charges_maximum: Maximum power charges.
    :param frenzy_charges: Frenzy charges.
    :param frenzy_charges_maximum: Maximum frenzy charges.
    :param endurance_charges: Endurance charges.
    :param endurance_charges_maximum: Maximum endurance charges.
    :param active_totem_limit: Maximum active totems.
    :param active_minion_limit: Maximum number of minions."""
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
