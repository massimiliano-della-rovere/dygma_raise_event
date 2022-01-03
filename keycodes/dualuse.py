from .functions import MODIFIERS, with_modifiers


from .digits import DIGITS
from .fxs import FX_KEYS
from .letters import LETTERS
from .miscellaneous import MISCELLANEOUS
from .navigation import NAVIGATION
from .numpad import NUMPAD
from .punctuation import PUNCTUATION
from .spacing import SPACING


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/dualuse.js
"""


KEY_GROUPS = (
    LETTERS, DIGITS, PUNCTUATION, SPACING, NAVIGATION, FX_KEYS, NUMPAD,
    MISCELLANEOUS)


DUAL_USE_MODIFIER = tuple(
    with_modifiers(
        key_group=key_group,
        group_name=modifier_info.group_name,
        label_top=modifier_info.label_top,
        bit_mask=48913 + modifier_info.bit_mask)
    for modifier_info in MODIFIERS
    for key_group in KEY_GROUPS)


DUAL_USE_LAYER = tuple(
    with_modifiers(
        key_group=key_group,
        group_name=f"Layer #{layer_index} /",
        label_top=f"L#{layer_index}/",
        bit_mask=50962 + 256 * layer_index)
    for layer_index in range(1, 11)
    for key_group in KEY_GROUPS)
