from __future__ import annotations


import abc
import copy
import itertools
import typing


from constants import (
    CHARSET, LAYERS_CUSTOM_QUANTITY, KeyboardLayout,
    LedPosition, LEDS_QUANTITY, MacroCode, PALETTE_SIZE, Side)
from keycodes.key import KeyDefinition


class IndexedColor(int):
    def render_for_command(self) -> bytes:
        return str(self).encode(CHARSET)

    def __copy__(self):
        return self

    def __deepcopy__(self, memo):
        return self


class RGBColor(typing.NamedTuple):
    r: int
    g: int
    b: int

    def __index__(self) -> int:
        return self.r << 16 + self.g << 8 + self.b

    def __hex__(self) -> int:
        return self.__index__()

    def __str__(self) -> str:
        return f"0x{self.r:02X}{self.g:02X}{self.b:02X}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.r}, {self.g}, {self.b})"

    def render_for_command(self) -> bytes:
        return f"{self.r} {self.g} {self.b}".encode(CHARSET)

    def __copy__(self):
        return RGBColor(self.r, self.g, self.b)

    def __deepcopy__(self, memo):
        return RGBColor(self.r, self.g, self.b)


Color = typing.TypeVar("Color", IndexedColor, RGBColor)


class ColorSet(metaclass=abc.ABCMeta):
    def __init__(self, colors: typing.Iterable[Color]):
        self._colors = list(colors)
        if len(self._colors) != self.size:
            raise ValueError

    def __str__(self) -> str:
        return str(self._colors)

    def __repr__(self) -> str:
        return f"{type(self).__name__}" \
               f"({', '.join(repr(x) for x in self._colors)})"

    @property
    @abc.abstractmethod
    def size(self) -> int:
        raise NotImplementedError

    def __len__(self) -> int:
        return len(self._colors)

    @typing.overload
    def __getitem__(self, key: int) -> Color:
        ...

    @typing.overload
    def __getitem__(self, key: slice) -> typing.Sequence[Color]:
        ...

    def __getitem__(self, key):
        return self._colors[key]

    @typing.overload
    def __setitem__(self, key: int, value: Color) -> None:
        ...

    @typing.overload
    def __setitem__(self, key: slice, value: typing.Sequence[Color]) -> None:
        ...

    def __setitem__(self, key, value):
        if isinstance(value, (IndexedColor, RGBColor)):
            self._colors[key] = value
        elif isinstance(value, slice):
            if value.step != 1:
                raise ValueError("step")
            self._colors = list(
                itertools.chain(
                    self._colors[:value.start],
                    value,
                    self._colors[value.stop:]))
        else:
            raise ValueError

    def __iter__(self) -> typing.Iterator[Color]:
        return iter(self._colors)

    def render_for_command(self) -> bytes:
        return b" ".join(color.render_for_command() for color in self._colors)

    def __copy__(self) -> ColorSet:
        return type(self)(copy.copy(color) for color in self._colors)

    def __deepcopy__(self, memo) -> ColorSet:
        return type(self)(copy.deepcopy(color) for color in self._colors)


class ColorPalette(ColorSet):
    @property
    def size(self) -> int:
        return PALETTE_SIZE


class KeyCoordinates(typing.NamedTuple):
    keyboard_layout: KeyboardLayout
    side: Side
    offset: int  # its offset in the list returned by DygmaRaiseAttributes
    row: int
    column: int  # relative to the leftmost key in the side


Layer = typing.Sequence[int]


T = typing.Type["T"]


class Layers:
    def __init__(self, values: typing.Iterable[T]):
        self._layers = list(values)
        if len(self._layers) != LAYERS_CUSTOM_QUANTITY:
            raise ValueError

    def __len__(self) -> int:
        return len(self._layers)

    def __getitem__(self, key: int) -> T:
        return self._layers[key]

    def __setitem__(self, key: int, value: T):
        self._layers[key] = T

    def __str__(self) -> str:
        return f"{type(self).__name__}({self._layers!s})"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._layers!r})"

    def __copy__(self) -> Layers:
        return type(self)(copy.copy(self._layers))

    def __deepcopy__(self, memo) -> Layers:
        return type(self)(copy.deepcopy(self._layers))

    def render_for_command(self) -> bytes:
        return b" ".join(
            layer.render_for_command()
            for layer in self._layers)


class LedCoordinates(typing.NamedTuple):
    keyboard_layout: KeyboardLayout
    side: Side
    offset: int  # its offset in the list returned by DygmaRaiseAttributes
    row: typing.Union[int, None]
    column: typing.Union[int, None]  # relative to the leftmost key in the side
    position: LedPosition


class LedLayout(ColorSet):
    @property
    def size(self) -> int:
        return LEDS_QUANTITY


class MacroItem(typing.NamedTuple):
    macro_code: MacroCode
    value: int | KeyDefinition

    def render_for_command(self) -> bytes:
        if self.macro_code == MacroCode.DELAY:
            value = f"{self.value >> 8} {self.value & 0xFF}"
        else:
            value = self.value
        return f"{self.macro_code.value} {value}".encode(CHARSET)


class Macro:
    def __init__(self, macro_items: typing.Iterable[MacroItem]):
        self._macro_items = tuple(macro_items)

    def __len__(self) -> int:
        return len(self._macro_items)

    def __getitem__(self, key: int) -> T:
        return self._macro_items[key]

    def __str__(self) -> str:
        return f"{type(self).__name__}({self._macro_items!s})"

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self._macro_items!r})"

    def __copy__(self) -> Macro:
        return type(self)(copy.copy(self._macro_items))

    def __deepcopy__(self, memo) -> Macro:
        return type(self)(copy.deepcopy(self._macro_items))

    def render_for_command(self) -> bytes:
        ret = bytearray(
            b" ".join(
                macro_item.render_for_command()
                for macro_item in self._macro_items))
        ret.extend(b" 0")
        return bytes(ret)


class Superkey(typing.NamedTuple):
    tap: int
    hold: int
    tap_hold: int
    double_tap: int
    double_tap_hold: int


class VersionType(typing.NamedTuple):
    bazecor_version: str
    kaleidoscope_newest_git_commit_id: str
    raise_firmware_newest_git_commit_id: str
