from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/ledeffects.js
"""


LED_EFFECTS = KeyGroup(
    name="LED Effect",
    keys=tuple(
        KeyDefinition(
            code=17152 + index,
            label=KeyLabel(top="LED", primary=label, verbose=""))
        for index, label in enumerate(("NEXT", "PREV", "TOGGLE"))))
