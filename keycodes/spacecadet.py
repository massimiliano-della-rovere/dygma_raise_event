from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/spacecadet.js
"""


SPACECADET = KeyGroup(
    name="Spacecadet",
    keys=tuple(
        KeyDefinition(
            code=53591 + index,
            label=KeyLabel(top="SCadet", primary=primary, verbose=""))
        for index, primary in enumerate(("ENABLE", "DISABLE"))))
