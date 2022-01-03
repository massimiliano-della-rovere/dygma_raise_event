from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/superkeys.js
"""


SUPERKEYS = KeyGroup(
    name="SuperKeys",
    keys=tuple(
        KeyDefinition(
            code=53916 + index,
            label=KeyLabel(top="SUPER", primary=str(1 + index), verbose=""))
        for index in range(64)))
