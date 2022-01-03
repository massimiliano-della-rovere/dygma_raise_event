from .functions import ModifierBitMask, MODIFIERS_POWERSET, with_modifiers
from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/punctuation.js
"""


PUNCTUATION = KeyGroup(
    name="Punctuation",
    keys=tuple(
        KeyDefinition(
            code=code,
            label=KeyLabel(top="Punctuation", primary=primary, verbose=verbose))
        for code, primary, verbose in ((45, "-", ""),
                                       (46, "=", ""),
                                       (47, "[", ""),
                                       (48, "]", ""),
                                       (49, "\\", ""),
                                       (51, ";", ""),
                                       (52, "'", ""),
                                       (53, "`", ""),
                                       (54, ",", ""),
                                       (55, ".", ""),
                                       (56, "/", ""),
                                       (57, "⇪", "Caps Lock"),
                                       (100, "<>", "ISO <>"))))

SHIFTED_PUNCTUATION = KeyGroup(
    name="Punctuation",
    keys=tuple(
        KeyDefinition(
            code=code,
            label=KeyLabel(top="Punctuation", primary=primary, verbose=verbose))
        for code, primary, verbose in ((2093, "-", ""),
                                       (2094, "+", ""),
                                       (2095, "{", ""),
                                       (2096, "}", ""),
                                       (2097, "|", ""),
                                       (2099, ":", ""),
                                       (2100, '"', ""),
                                       (2101, "~", ""),
                                       (2102, "<", ""),
                                       (2103, ">", ""),
                                       (2104, "?", ""),
                                       (2148, "Alt. |", "Non-US |"))))

MODIFIED_PUNCTUATION = tuple(
    with_modifiers(
        key_group=(
            SHIFTED_PUNCTUATION
            if modifier_info.bit_mask == ModifierBitMask.SHIFT
            else PUNCTUATION),
        group_name=modifier_info.group_name,
        label_top=modifier_info.label_top,
        bit_mask=modifier_info.bit_mask)
    for modifier_info in MODIFIERS_POWERSET)
