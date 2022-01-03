from .functions import MODIFIERS_POWERSET, with_modifiers
from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/mediacontrols.js
"""


MISCELLANEOUS = KeyGroup(
    name="Miscellaneous",
    keys=(
        KeyDefinition(
            code=70,
            label=KeyLabel(
                top="",
                primary="PRINT SCRN",
                verbose="Print Screen")),
        KeyDefinition(
            code=71,
            label=KeyLabel(
                top="",
                primary="SCROLL LCK",
                verbose="Scroll Lock")),
        KeyDefinition(
            code=72,
            label=KeyLabel(
                top="",
                primary="PAUSE",
                verbose="")),
        KeyDefinition(
            code=53291,
            label=KeyLabel(
                top="",
                primary="CYCLE",
                verbose="")),
        KeyDefinition(
            code=53292,
            label=KeyLabel(
                top="",
                primary="SYSTER",
                verbose=""))))


MODIFIED_MISCELLANEOUS = tuple(
    with_modifiers(
        key_group=MISCELLANEOUS,
        group_name=modifier_info.group_name,
        label_top=modifier_info.label_top,
        bit_mask=modifier_info.bit_mask)
    for modifier_info in MODIFIERS_POWERSET)
