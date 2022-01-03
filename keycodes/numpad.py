from .functions import MODIFIERS_POWERSET, with_modifiers
from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/numpad.js
"""


NUMPAD = KeyGroup(
    name="Numpad",
    keys=tuple(
        KeyDefinition(
            code=83 + index,
            label=KeyLabel(top="Num", primary=primary, verbose=""))
        for index, primary in enumerate(("Num Lock",
                                         "/",
                                         "*",
                                         "-",
                                         "+",
                                         "Enter",
                                         "1",
                                         "2",
                                         "3",
                                         "4",
                                         "5",
                                         "6",
                                         "7",
                                         "8",
                                         "9",
                                         "0",
                                         "."))))

MODIFIED_NUMPAD = tuple(
    with_modifiers(
        key_group=NUMPAD,
        group_name=modifier_info.group_name,
        label_top=modifier_info.label_top,
        bit_mask=modifier_info.bit_mask)
    for modifier_info in MODIFIERS_POWERSET)
