import enum


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
