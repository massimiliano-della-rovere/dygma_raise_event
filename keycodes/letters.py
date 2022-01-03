from .functions import MODIFIERS_POWERSET, with_modifiers
from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/letters.js
"""


LETTERS = KeyGroup(
    name="Letters",
    keys=tuple(
        KeyDefinition(
            code=4 + index,
            label=KeyLabel(top="", primary=letter.upper(), verbose=""))
        for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz")))


MODIFIED_LETTERS = tuple(
    with_modifiers(
        key_group=LETTERS,
        group_name=modifier_info.group_name,
        label_top=modifier_info.label_top,
        bit_mask=modifier_info.bit_mask)
    for modifier_info in MODIFIERS_POWERSET)
