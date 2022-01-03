from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/mousecontrols.js
"""


MOUSE_MOVEMENT = KeyGroup(
    name="Mouse movement",
    keys=tuple(
        KeyDefinition(
            code=code,
            label=KeyLabel(top="MOUSE", primary=direction, verbose=""))
        for code, direction in ((20481, "UP"),
                                (20482, "DOWN"),
                                (20484, "LEFT"),
                                (20488, "RIGHT"))))


MOUSE_WHEEL = KeyGroup(
    name="Mouse wheel",
    keys=tuple(
        KeyDefinition(
            code=code,
            label=KeyLabel(top="M.Wheel", primary=direction, verbose=""))
        for code, direction in ((20497, "UP"),
                                (20498, "DOWN"),
                                (20500, "LEFT"),
                                (20504, "RIGHT"))))


MOUSE_BUTTONS = KeyGroup(
    name="Mouse button",
    keys=tuple(
        KeyDefinition(
            code=code,
            label=KeyLabel(top="M.Btn", primary=direction, verbose=""))
        for code, direction in ((20545, "LEFT"),
                                (20546, "RIGHT"),
                                (20548, "MIDDLE"),
                                (20552, "BACK"),
                                (20560, "FORW."))))


MOUSE_WARP = KeyGroup(
    name="Mouse warp",
    keys=tuple(
        KeyDefinition(
            code=code,
            label=KeyLabel(top="M.Warp", primary=primary, verbose=verbose))
        for code, primary, verbose in ((20576, "END", ""),
                                       (20517, "NW", "North-West"),
                                       (20518, "SW", "South-West"),
                                       (20521, "NE", "North-East"),
                                       (20522, "SE", "South-East"))))
