import itertools


from .blanks import BLANKS
from .digits import DIGITS, MODIFIED_DIGITS
from .dualuse import DUAL_USE_LAYER, DUAL_USE_MODIFIER
from .fxs import FX_KEYS, MODIFIED_FX_KEYS
from .layerswitch import LOCK_LAYER_TO, MOVE_TO_LAYER, SHIFT_TO_LAYER
from .leader import LEADER
from .ledeffects import LED_EFFECTS
from .letters import LETTERS, MODIFIED_LETTERS
from .macros import MACROS
from .media_controls import MEDIA_CONTROLS
from .miscellaneous import MISCELLANEOUS, MODIFIED_MISCELLANEOUS
from .modifiers import MODIFIERS, MODIFIED_MODIFIERS
from .mouse_controls import (
    MOUSE_BUTTONS, MOUSE_MOVEMENT, MOUSE_WARP, MOUSE_WHEEL)
from .navigation import NAVIGATION, MODIFIED_NAVIGATION
from .numpad import NUMPAD, MODIFIED_NUMPAD
from .oneshot import ONESHOT_LAYERS, ONESHOT_MODIFIERS
from .punctuation import PUNCTUATION, MODIFIED_PUNCTUATION
from .spacecadet import SPACECADET
from .spacing import SPACING, MODIFIED_SPACING
from .steno import STENO
from .superkeys import SUPERKEYS
from .tapdance import TAPDANCE


KEY_CODES = {
    key_definition.code: key_definition
    for key_group in itertools.chain((
            BLANKS,

            DIGITS, LETTERS, SPACING, PUNCTUATION,

            FX_KEYS, MISCELLANEOUS, NAVIGATION, NUMPAD,

            MACROS, SUPERKEYS, STENO, TAPDANCE,

            MOUSE_BUTTONS, MOUSE_MOVEMENT, MOUSE_WARP, MOUSE_WHEEL,

            LED_EFFECTS, MEDIA_CONTROLS,

            LEADER, MODIFIERS, SPACECADET,

            LOCK_LAYER_TO, MOVE_TO_LAYER, SHIFT_TO_LAYER,

            ONESHOT_LAYERS, ONESHOT_MODIFIERS,
            *DUAL_USE_LAYER, *DUAL_USE_MODIFIER,

            *MODIFIED_DIGITS,
            *MODIFIED_FX_KEYS,
            *MODIFIED_LETTERS,
            *MODIFIED_MISCELLANEOUS,
            *MODIFIED_MODIFIERS,
            *MODIFIED_NAVIGATION,
            *MODIFIED_NUMPAD,
            *MODIFIED_PUNCTUATION,
            *MODIFIED_SPACING))
    for key_definition in iter(key_group.keys)
}

# print(
#     *tuple(
#         (item.code, item.label)
#         for item in sorted(KEY_CODES.values(), key=lambda item: item.code)),
#     sep="\n")
# exit(0)
