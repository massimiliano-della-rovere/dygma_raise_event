from .functions import ModifierBitMask, MODIFIERS_POWERSET, with_modifiers
from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/digits.js
"""


DIGITS = KeyGroup(
    name="Digits",
    keys=tuple(
        KeyDefinition(
            code=30 + index,
            label=KeyLabel(top="", primary=number, verbose=""))
        for index, number in enumerate("1234567890")))


SHIFTED_DIGITS = KeyGroup(
    name="Shifted Digits",
    keys=tuple(
        KeyDefinition(
            code=2078 + index,
            label=KeyLabel(top="", primary=symbol, verbose=""))
        for index, symbol in enumerate("!@#$%^&*()")))


MODIFIED_DIGITS = tuple(
    with_modifiers(
        key_group=(
            SHIFTED_DIGITS
            if modifier_info.bit_mask == ModifierBitMask.SHIFT
            else DIGITS),
        group_name=modifier_info.group_name,
        label_top=modifier_info.label_top,
        bit_mask=modifier_info.bit_mask)
    for modifier_info in MODIFIERS_POWERSET)
