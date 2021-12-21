"""Key and LED maps for ANSI and ISO layouts."""


import abc
import itertools
import typing


from auxilary_types import KeyCoordinates, LedCoordinates
from constants import KeyboardLayout, LedPosition, Side


class Layout(metaclass=abc.ABCMeta):
    def __init__(self, keyboard_layout: KeyboardLayout):
        self._keyboard_layout = keyboard_layout
        self._layout = self.generate_layout(keyboard_layout)

    @staticmethod
    @abc.abstractmethod
    def generate_layout(keyboard_layout: KeyboardLayout) \
            -> dict[int, typing.Any]:
        raise NotImplementedError


_LED_LAYOUT_META = {
    KeyboardLayout.ANSI: (
        {
            Side.LEFT: tuple(range(0, 7)),
            Side.RIGHT: tuple(range(9, 16))
        },
        {
            Side.LEFT: tuple(range(16, 21)),
            Side.RIGHT: tuple(itertools.chain(range(24, 31), (47,)))
        },
        {
            Side.LEFT: tuple(range(32, 37)),
            Side.RIGHT: tuple(itertools.chain(range(41, 47), (31,)))
        },
        {
            Side.LEFT: tuple(i for i in range(48, 54) if i != 49),
            Side.RIGHT: tuple(range(58, 64))
        },
        {
            Side.LEFT: tuple(range(64, 69)),
            Side.RIGHT: tuple(range(74, 80))},
        {
            Side.LEFT: (70, 71),
            Side.RIGHT: (72, 73)
        }),
    KeyboardLayout.ISO: (
        {
            Side.LEFT: tuple(range(0, 7)),
            Side.RIGHT: tuple(range(9, 16))
        },
        {
            Side.LEFT: tuple(range(16, 21)),
            Side.RIGHT: tuple(range(24, 32))
        },
        {
            Side.LEFT: tuple(range(32, 37)),
            Side.RIGHT: tuple(range(41, 48))
        },
        {
            Side.LEFT: tuple(range(48, 55)),
            Side.RIGHT: tuple(range(58, 64))
        },
        {
            Side.LEFT: tuple(range(64, 69)),
            Side.RIGHT: tuple(range(74, 80))
        },
        {
            Side.LEFT: (70, 71),
            Side.RIGHT: (72, 73)
        })
}


class KeyLayout(Layout):
    @staticmethod
    def generate_layout(keyboard_layout: KeyboardLayout) \
            -> typing.TypedDict[str, KeyCoordinates]:
        layout_meta = _LED_LAYOUT_META[keyboard_layout]
        layout = {}
        for row, left_right_offsets in enumerate(layout_meta):
            for side, side_offsets in left_right_offsets.items():
                for column, offset in enumerate(side_offsets):
                    layout[offset] = KeyCoordinates(
                        keyboard_layout=keyboard_layout,
                        offset=offset,
                        side=side,
                        row=row,
                        column=column)
        return layout

    @property
    def keyboard_layout(self) -> KeyboardLayout:
        return self._keyboard_layout


_KEY_LAYOUT_META = {
    KeyboardLayout.ANSI: (
        {
            Side.LEFT: tuple(range(0, 7)),
            Side.RIGHT: tuple(range(33, 40))
        },
        {
            Side.LEFT: tuple(range(7, 13)),
            Side.RIGHT: tuple(range(47, 39, -1))
        },
        {
            Side.LEFT: tuple(range(13, 19)),
            Side.RIGHT: tuple(range(54, 47, -1))
        },
        {
            Side.LEFT: tuple(i for i in range(19, 26) if i != 20),
            Side.RIGHT: tuple(range(60, 54, -1))
        },
        {
            Side.LEFT: tuple(range(26, 30)),
            Side.RIGHT: tuple(range(66, 60, -1))
        },
        {
            Side.LEFT: (31, 32),
            Side.RIGHT: (68, 67)
        },
        {
            Side.LEFT: tuple(range(69, 99)),
            Side.RIGHT: tuple(range(99, 131))
        },
        {Side.NEURON: (131,)}),
    KeyboardLayout.ISO: (
        {
            Side.LEFT: tuple(range(0, 7)),
            Side.RIGHT: tuple(range(33, 40))
        },
        {
            Side.LEFT: tuple(range(7, 13)),
            Side.RIGHT: tuple(range(47, 39, -1))
        },
        {
            Side.LEFT: tuple(range(13, 19)),
            Side.RIGHT: tuple(range(54, 47, -1))
        },
        {
            Side.LEFT: tuple(range(19, 26)),
            Side.RIGHT: tuple(range(60, 54, -1))
        },
        {
            Side.LEFT: tuple(range(26, 30)),
            Side.RIGHT: tuple(range(66, 60, -1))},
        {
            Side.LEFT: (31, 32),
            Side.RIGHT: (68, 67)
        },
        {
            Side.LEFT: tuple(range(69, 99)),
            Side.RIGHT: tuple(range(99, 131))
        },
        {Side.NEURON: (131,)})
}


class LedLayout(Layout):
    @staticmethod
    def generate_layout(keyboard_layout: KeyboardLayout) \
            -> typing.TypedDict[str, LedCoordinates]:
        layout_meta = _KEY_LAYOUT_META[keyboard_layout]
        base_index = len(layout_meta) - 1
        layout = {}
        for row, left_right_offsets in enumerate(layout_meta):
            for side, side_offsets in left_right_offsets.items():
                for column, offset in enumerate(side_offsets):
                    if side is Side.NEURON:
                        position = LedPosition.NEURON
                        is_key = False
                    else:
                        if row < base_index:
                            position = LedPosition.KEY
                            is_key = True
                        else:
                            position = LedPosition.BASE
                            is_key = False
                    layout[offset] = LedCoordinates(
                        keyboard_layout=keyboard_layout,
                        offset=offset,
                        side=side,
                        row=row if is_key else None,
                        column=column if is_key else None,
                        position=position)
        return layout
