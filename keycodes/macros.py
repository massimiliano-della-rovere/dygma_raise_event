from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/macros.js
"""


MACROS = KeyGroup(
    name="Macros",
    keys=tuple(
        KeyDefinition(
            code=53852 + index,
            label=KeyLabel(top="MACRO", primary=str(index), verbose=""))
        for index in range(64)))
