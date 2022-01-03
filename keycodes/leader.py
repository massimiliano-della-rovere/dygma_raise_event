from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/leader.js
"""


LEADER = KeyGroup(
    name="Leader",
    keys=tuple(
        KeyDefinition(
            code=53283 + index,
            label=KeyLabel(top="Leader", primary=f"#{index}", verbose=""))
        for index in range(8)))
