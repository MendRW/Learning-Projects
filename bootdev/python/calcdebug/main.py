def take_magic_damage(health, resist, amp, spell_power):
    spellcalc = spell_power * amp
    resistcalc = spellcalc - resist
    damagecalc = health - resistcalc
    return damagecalc
    