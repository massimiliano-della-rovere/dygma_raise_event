from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/blanks.js
"""


BLANKS = KeyGroup(
    name="Blank",
    keys=(
        KeyDefinition(  # NoKey
            code=0,
            label=KeyLabel(top="NO", primary="KEY", verbose="Disabled")),
        KeyDefinition(  # Transparent
            code=65535,
            label=KeyLabel(top="TRANS", primary="", verbose="Disabled"))))
