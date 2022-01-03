import itertools
import platform
import typing


from .functions import ModifierBitMask, MODIFIERS_POWERSET, with_modifiers
from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/modifiers.js
"""


class OSLabels(typing.NamedTuple):
    linux: str
    windows: str
    darwin: str


GUI_LABELS = OSLabels(linux="LINUX", windows="WIN", darwin="⌘")
GUI_VERBOSES = OSLabels(linux="Linux", windows="Windows", darwin="Command")

ALT_LABELS = OSLabels(linux="ALT", windows="ALT", darwin="⌥")
ALT_VERBOSES = OSLabels(linux="Alt", windows="Alt", darwin="Option")


_os_id = platform.system().lower()

_gui_attribute = _os_id or "Gui"
GUI_LABEL = getattr(GUI_LABELS, _gui_attribute)
GUI_VERBOSE = getattr(GUI_VERBOSES, _gui_attribute)

_alt_attribute = _os_id or "ALT"
ALT_LABEL = getattr(ALT_LABELS, _alt_attribute)
ALT_VERBOSE = getattr(ALT_VERBOSES, _alt_attribute)


MODIFIERS = KeyGroup(
    name="Shifted Digits",
    keys=tuple(
        KeyDefinition(
            code=224 + index,
            label=key_label)
        for index, key_label in enumerate((
            KeyLabel(
                top="LEFT",
                primary="CTRL",
                verbose="Left Control"),
            KeyLabel(
                top="LEFT",
                primary="SHIFT",
                verbose="Left Shift"),
            KeyLabel(
                top="",
                primary=f"LEFT {ALT_LABEL}",
                verbose=f"LEFT {ALT_VERBOSE}"),
            KeyLabel(
                top="",
                primary=f"LEFT {GUI_LABEL}",
                verbose=f"LEFT {GUI_VERBOSE}"),

            KeyLabel(
                top="RIGHT",
                primary="CTRL",
                verbose="Right Control"),
            KeyLabel(
                top="RIGHT",
                primary="SHIFT",
                verbose="Right Shift"),
            KeyLabel(
                top="",
                primary=f"RIGHT {ALT_LABEL}",
                verbose=f"AltGr"),
            KeyLabel(
                top="",
                primary=f"RIGHT {GUI_LABEL}",
                verbose=f"RIGHT {GUI_VERBOSE}")))))


HYPER_AND_MEH = KeyGroup(
    name="Shifted Digits",
    keys=(
        KeyDefinition(
            code=2530,
            label=KeyLabel(top="", primary="Meh", verbose="")),
        KeyDefinition(
            code=3043,
            label=KeyLabel(top="", primary="Hyper", verbose=""))))


MODIFIED_MODIFIERS = tuple(
    itertools.chain(
        with_modifiers(
            key_group=key_group,
            group_name=modifier_info.group_name,
            label_top=modifier_info.label_top,
            bit_mask=modifier_info.bit_mask)
        for modifier_info in MODIFIERS_POWERSET
        for key_group in (MODIFIERS, HYPER_AND_MEH)))
