# Built-ins
from dataclasses import dataclass
# Third-party
from dataslots import with_slots

__all__ = ["Stats"]


@with_slots
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
