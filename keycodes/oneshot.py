from .key import KeyDefinition, KeyGroup, KeyLabel
from .modifiers import GUI_LABEL


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/oneshot.js
"""


ONESHOT_MODIFIERS = KeyGroup(
    name="Oneshot modifiers",
    keys=tuple(
        KeyDefinition(
            code=49153 + index,
            label=KeyLabel(
                top="OSM", 
                primary=verbose.upper() if verbose != "AltGr" else "RIGHT ALT",
                verbose=verbose))
        for index, verbose in enumerate((
            "Left Control",
            "Left Shift",
            "Left Alt",
            f"Left {GUI_LABEL}",
            "Right Control",
            "Right Shift",
            "AltGr",
            f"Right {GUI_LABEL}"))))


ONESHOT_LAYERS = KeyGroup(
    name="Oneshot layers",
    keys=tuple(
        KeyDefinition(
            code=49161 + index,
            label=KeyLabel(
                top="OSL",
                primary=str(index),
                verbose=""))
        for index in range(1, 11)))
