from .functions import MODIFIERS_POWERSET, with_modifiers
from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/punctuation.js
"""


SPACING = KeyGroup(
    name="Spacing",
    keys=tuple(
        KeyDefinition(
            code=code,
            label=KeyLabel(top="Punctuation", primary=primary, verbose=verbose))
        for code, primary, verbose in ((40, "ENTER", ""),
                                       (41, "ESC", ""),
                                       (42, "BACKSPACE", "Backspace"),
                                       (43, "TAB", ""),
                                       (44, "SPACE", ""),
                                       (73, "INSERT", ""),
                                       (76, "DEL", ""))))

MODIFIED_SPACING = tuple(
    with_modifiers(
        key_group=SPACING,
        group_name=modifier_info.group_name,
        label_top=modifier_info.label_top,
        bit_mask=modifier_info.bit_mask)
    for modifier_info in MODIFIERS_POWERSET)
