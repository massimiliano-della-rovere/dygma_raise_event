import enum


"""
TODO: import constants:
https://github.com/Dygmalab/Bazecor/tree/development/src/api/keymap/db
"""


CHARSET = "ascii"


PALETTE_SIZE = 16
LAYERS_CUSTOM_QUANTITY = 10
LAYERS_DEFAULT_QUANTITY = 2
LAYERS_TOTAL_QUANTITY = LAYERS_DEFAULT_QUANTITY + LAYERS_CUSTOM_QUANTITY
LEDS_QUANTITY = 132
KEYMAPS_QUANTITY_IN_COMMAND = 80
KEYMAPS_ANSI_QUANTITY = 68
KEYMAPS_ISO_QUANTITY = 69


class KeyboardLayout(enum.Enum):
    ANSI = "ANSI"
    ISO = "ISO"


class LedEffect(enum.Enum):
    NORMAL = 0
    RAINBOW = 1
    BREATHING = 2
    OFF = 3


class LedPosition(enum.Enum):
    KEY = "key"
    BASE = "base"
    NEURON = "neuron"


class Side(enum.Enum):
    LEFT = "left"
    RIGHT = "right"
    NEURON = "neuron"


class MacroCode(enum.IntEnum):
    END = 0  # 1-byte payload
    DELAY = 2  # 2-bytes payload
    FUNCTION_KEY_PRESS = 3  # 1-byte payload
    FUNCTION_KEY_RELEASE = 4  # 1-byte payload
    FUNCTION_KEY_PRESS_RELEASE = 5  # 1-byte payload
    KEY_CODE_PRESS = 6  # 1-byte payload
    KEY_CODE_RELEASE = 7  # 1-byte payload
    KEY_CODE_PRESS_RELEASE = 8  # 1-byte payload


MACRO_VALUES = tuple(v.value for v in MacroCode.__members__.values())
