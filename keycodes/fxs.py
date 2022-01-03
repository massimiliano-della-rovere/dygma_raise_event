from .functions import MODIFIERS_POWERSET, with_modifiers
from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/fxs.js
"""


FX_KEYS = KeyGroup(
    name="Fx keys",
    keys=tuple(
        KeyDefinition(
            code=58 + number,
            label=KeyLabel(top="", primary=f"F{number}", verbose=""))
        for number in range(1, 25)))


MODIFIED_FX_KEYS = tuple(
    with_modifiers(
        key_group=FX_KEYS,
        group_name=modifier_info.group_name,
        label_top=modifier_info.label_top,
        bit_mask=modifier_info.bit_mask)
    for modifier_info in MODIFIERS_POWERSET)
