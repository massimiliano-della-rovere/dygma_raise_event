from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/layerswitch.js
"""


LOCK_LAYER_TO = KeyGroup(
    name="Lock layer to",
    keys=tuple(
        KeyDefinition(
            code=17407 + number,
            label=KeyLabel(top="LockTo", primary=str(number), verbose=""))
        for number in range(1, 11)))


SHIFT_TO_LAYER = KeyGroup(
    name="Shift to layer",
    keys=tuple(
        KeyDefinition(
            code=17449 + number,
            label=KeyLabel(top="SWITCH", primary=str(number), verbose=""))
        for number in range(1, 11)))


MOVE_TO_LAYER = KeyGroup(
    name="Move to layer",
    keys=tuple(
        KeyDefinition(
            code=17491 + number,
            label=KeyLabel(top="LOCK", primary=str(number), verbose=""))
        for number in range(1, 11)))
