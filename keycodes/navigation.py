from .functions import MODIFIERS_POWERSET, with_modifiers
from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/navigation.js
"""


NAVIGATION = KeyGroup(
    name="Navigation",
    keys=tuple(
        KeyDefinition(
            code=code,
            label=KeyLabel(top="", primary=direction, verbose=""))
        for code, direction in ((74, "Home"),
                                (75, "Page Up"),
                                (77, "End"),
                                (78, "Page Down"),
                                (79, "→"),
                                (80, "←"),
                                (81, "↓"),
                                (82, "↑"),
                                (101, "MENU"))))

MODIFIED_NAVIGATION = tuple(
    with_modifiers(
        key_group=NAVIGATION,
        group_name=modifier_info.group_name,
        label_top=modifier_info.label_top,
        bit_mask=modifier_info.bit_mask)
    for modifier_info in MODIFIERS_POWERSET)
