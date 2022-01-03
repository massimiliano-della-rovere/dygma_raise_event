from .key import KeyDefinition, KeyGroup, KeyLabel


"""
porting of 
https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/steno.js
"""


STENO = KeyGroup(
    name="Steno",
    keys=tuple(
        KeyDefinition(
            code=53549 + index,
            label=KeyLabel(top="Steno", primary=primary, verbose=""))
        for index, primary in enumerate(("FN",
                                         "N1",
                                         "N2",
                                         "N3",
                                         "N4",
                                         "N5",
                                         "N6",
                                         "S1",
                                         "S2",
                                         "TL",
                                         "KL",
                                         "PL",
                                         "WL",
                                         "HL",
                                         "RL",
                                         "A",
                                         "O",
                                         "ST1",
                                         "ST2",
                                         "RE1",
                                         "RE2",
                                         "PWR",
                                         "ST3",
                                         "ST4",
                                         "E",
                                         "U",
                                         "FR",
                                         "RR",
                                         "PR",
                                         "BR",
                                         "LR",
                                         "GR",
                                         "TR",
                                         "SR",
                                         "DR",
                                         "N7",
                                         "N8",
                                         "N9",
                                         "NA",
                                         "NB",
                                         "NC",
                                         "ZR"))))
