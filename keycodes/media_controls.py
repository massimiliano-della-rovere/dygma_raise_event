from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/mediacontrols.js
"""


MEDIA_CONTROLS = KeyGroup(
    name="Media Controls",
    keys=(
        KeyDefinition(
            code=19682,
            label=KeyLabel(top="MUTE", primary="🔇", verbose="")),
        KeyDefinition(
            code=22709,
            label=KeyLabel(top="Next track", primary="⏭", verbose="")),
        KeyDefinition(
            code=22710,
            label=KeyLabel(top="Prev. track", primary="⏮", verbose="")),
        KeyDefinition(
            code=22711,
            label=KeyLabel(top="STOP", primary="⏹", verbose="")),
        KeyDefinition(
            code=22733,
            label=KeyLabel(top="Play / pause", primary="⏯", verbose="")),
        KeyDefinition(
            code=23785,
            label=KeyLabel(top="Volume up", primary="🔊", verbose="")),
        KeyDefinition(
            code=23786,
            label=KeyLabel(top="Volume down", primary="🔉", verbose="")),
        KeyDefinition(
            code=22712,
            label=KeyLabel(top="Eject", primary="⏏", verbose="")),
        KeyDefinition(
            code=18552,
            label=KeyLabel(top="", primary="Camera", verbose="")),
        KeyDefinition(
            code=23663,
            label=KeyLabel(top="Display", primary="Bright +", verbose="")),
        KeyDefinition(
            code=23664,
            label=KeyLabel(top="Display", primary="Bright -", verbose="")),
        KeyDefinition(
            code=18834,
            label=KeyLabel(top="Apps", primary="Calc", verbose="")),
        KeyDefinition(
            code=22713,
            label=KeyLabel(top="", primary="Shuff.", verbose=""))))
