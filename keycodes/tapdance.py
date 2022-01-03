from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/tapdance.js
"""


TAPDANCE = KeyGroup(
    name="TapDance",
    keys=tuple(
        KeyDefinition(
            code=53267 + index,
            label=KeyLabel(top="TAPD", primary=str(index), verbose=""))
        for index in range(64)))
