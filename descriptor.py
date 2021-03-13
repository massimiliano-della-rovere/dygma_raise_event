"""Descriptors for the Dygma Raise class."""


from __future__ import annotations


import abc
import itertools
import typing


import serial


from auxilary_types import (
    ColorPalette, IndexedColor, Layers, LedLayout, RGBColor, VersionType)
from constants import (
    CHARSET, KEYMAPS_QUANTITY_IN_COMMAND, LedEffect, LEDS_QUANTITY)


if typing.TYPE_CHECKING:
    from dygma_raise import DygmaRaise


class DygmaRaiseBaseDescriptor(metaclass=abc.ABCMeta):
    def __set_name__(self, owner, name):
        self.name = name

    @property
    @abc.abstractmethod
    def command(self) -> bytes:
        raise NotImplementedError

    @staticmethod
    def output_cast(received_text: str, dr: DygmaRaise) -> str:
        return received_text

    def __get__(self, dr: DygmaRaise, objtype=None) -> typing.Any:
        return self.output_cast(received_text=next(self._io(dr)), dr=dr)

    def _io(self,
            dr: DygmaRaise,
            set_command_args: typing.Optional[bytes] = None) \
            -> typing.Generator[str, None, None]:
        with serial.Serial(dr.device) as connection:
            command = [self.command]
            if set_command_args:
                command.extend((b" ", set_command_args))
            command.append(b"\n")
            command = b"".join(command)
            connection.write(command)
            dr.logger.debug("sent: %s", command.decode(CHARSET).strip())
            while (received := connection.readline()
                    .strip()
                    .decode(CHARSET)) != ".":
                dr.logger.debug("received: %s", received)
                yield received

    @staticmethod
    def _extract_layers(received_text: str, slice_size: int) -> Layers:
        numeric_values = map(int, received_text.split(" "))
        while layer := tuple(
                itertools.islice(numeric_values, 0, slice_size)):
            yield layer

    def _extract_rgbmap_layers(self, received_text: str) -> Layers:
        for layer in self._extract_layers(received_text,
                                          slice_size=LEDS_QUANTITY):
            yield LedLayout(
                RGBColor._make(r_g_b)
                for r_g_b in itertools.islice(layer, 0, 3))

    def _extract_keymap_layers(self, received_text: str) -> Layers:
        yield from self._extract_layers(
            received_text,
            slice_size=KEYMAPS_QUANTITY_IN_COMMAND)

    def _extract_palettemap_layers(self, received_text: str) -> Layers:
        for layer in self._extract_layers(received_text,
                                          slice_size=LEDS_QUANTITY):
            yield LedLayout(IndexedColor(v) for v in layer)

    def _extract_color(self, received_text: str) -> Layers:
        for r_g_b in self._extract_layers(received_text, slice_size=3):
            yield RGBColor._make(r_g_b)

    @staticmethod
    def _extract_bool(received_text: str) -> bool:
        try:
            return {
                "false": False,
                "true": True
            }[received_text]
        except KeyError as e:
            # dr.logger.error("Unsupported value '%s'", received_text)
            raise ValueError(received_text) from e

    @staticmethod
    def _extract_int_tuple(received_text: str,
                           token: str = " ") -> typing.Sequence[int]:
        return tuple(map(int, received_text.split(token)))

    def __set__(self, dr: DygmaRaise, value: typing.Any) -> None:
        raise TypeError(f"property '{self.name}' is readonly")


class ColormapMap(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"colormap.map"

    def output_cast(self, received_text: str, dr: DygmaRaise) -> Layers:
        return Layers(self._extract_palettemap_layers(received_text))

    def __set__(self, dr: DygmaRaise, value: Layers):
        next(self._io(dr, set_command_args=value.render_for_command()))


class EEPROMContents(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"eeprom.contents"

    def output_cast(self,
                    received_text: str,
                    dr: DygmaRaise) -> typing.Sequence[int]:
        return self._extract_int_tuple(received_text)

    def __set__(self, instance: DygmaRaise, value: tuple[int]):
        raise NotImplementedError


class EEPROMFree(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"eeprom.free"

    def output_cast(self, received_text: str, dr: DygmaRaise) -> int:
        return int(received_text)


class HardwareCRCErrors(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"hardware.crc_errors"


class HardwareFirmware(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"hardware.firmware"


class HardwareJoint(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"hardware.joint"

    @staticmethod
    def output_cast(received_text: str, dr: DygmaRaise) -> int:
        return int(received_text)


class HardwareKeyscan(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"hardware.keyscan"

    @staticmethod
    def output_cast(received_text: str, dr: DygmaRaise) -> int:
        return int(received_text)


class HardwareLayout(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"hardware.layout"


class HardwareSidePower(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"hardware.side_power"

    @staticmethod
    def output_cast(received_text: str, dr: DygmaRaise) -> int:
        return int(received_text)


class HardwareSideVer(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"hardware.side_ver"


class HardwareSledCurrent(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"hardware.sled_current"


class HardwareSledVer(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"hardware.sled_ver"


class HardwareVersion(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"hardware.version"


class Help(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"help"


class IdleledsTimeLimit(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"idleleds.time_limit"

    @staticmethod
    def output_cast(received_text: str, dr: DygmaRaise) -> int:
        return int(received_text)

    def __set__(self, dr: DygmaRaise, value: Layers):
        next(self._io(dr, set_command_args=str(value).encode(CHARSET)))


class KeymapCustom(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"keymap.custom"

    def output_cast(self, received_text: str, dr: DygmaRaise) -> Layers:
        return tuple(self._extract_keymap_layers(received_text))

    def __set__(self, dr: DygmaRaise, value: Layers):
        next(self._io(dr, set_command_args=str(value).encode(CHARSET)))


class KeymapDefault(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"keymap.default"

    def output_cast(self, received_text: str) -> Layers:
        return tuple(self._extract_keymap_layers(received_text))

    def __set__(self, instance: DygmaRaise, value: tuple[int]):
        raise NotImplementedError


class KeymapOnlyCustom(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"keymap.onlyCustom"

    def output_cast(self, received_text: str, dr: DygmaRaise) -> bool:
        return self._extract_bool(received_text)

    def __set__(self,
                dr: DygmaRaise,
                value: bool) -> None:
        if not isinstance(value, bool):
            raise ValueError
        next(self._io(dr, set_command_args=str(int(value)).encode(CHARSET)))


class LedAt(DygmaRaiseBaseDescriptor):
    def __set_name__(self, owner, name):
        super().__set_name__(owner, name)
        led_id = int(name.rsplit("_", 1)[1])
        if 0 <= led_id < LEDS_QUANTITY:
            self._led_id = led_id
        else:
            raise ValueError("led_id")

    @property
    def led_id(self) -> int:
        return self._led_id

    @property
    def command(self) -> bytes:
        return b" ".join((b"led.at", str(self._led_id).encode(CHARSET)))

    def output_cast(self, received_text: str, dr: DygmaRaise) -> RGBColor:
        return next(self._extract_color(received_text))

    def __set__(self, dr: DygmaRaise, value: RGBColor) -> None:
        if value not in range(-2, 10):
            raise ValueError
        next(self._io(dr, set_command_args=value.render_for_command()))


class LedBrightness(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"led.brightness"

    @staticmethod
    def output_cast(received_text: str, dr: DygmaRaise) -> int:
        return int(received_text)

    def __set__(self, dr: DygmaRaise, value: int) -> None:
        next(self._io(dr, set_command_args=str(value).encode(CHARSET)))


class LedMode(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"led.mode"

    @staticmethod
    def output_cast(received_text: str, dr: DygmaRaise) -> LedEffect:
        return LedEffect(int(received_text))

    def __set__(self, dr: DygmaRaise, value: LedEffect) -> None:
        next(self._io(dr, set_command_args=str(value.value).encode(CHARSET)))


class LedSetAll(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"led.setAll"

    def __get__(self, dr: DygmaRaise, objtype=None) -> typing.Any:
        raise TypeError

    def __set__(self, dr: DygmaRaise, value: RGBColor) -> None:
        next(self._io(dr, set_command_args=value.render_for_command()))


class LedTheme(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"led.theme"

    def output_cast(self, received_text: str, dr: DygmaRaise) -> LedLayout:
        return LedLayout(self._extract_color(received_text))

    def __set__(self, dr: DygmaRaise, value: RGBColor) -> None:
        next(self._io(dr, set_command_args=value.render_for_command()))


class MacrosMap(DygmaRaiseBaseDescriptor):
    # TODO: Macros Map class
    @property
    def command(self) -> bytes:
        return b"macros.map"


class MacrosTrigger(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"macros.trigger"

    def __get__(self, dr: DygmaRaise, objtype=None) -> typing.Any:
        raise TypeError

    def __set__(self, dr: DygmaRaise, value: int) -> None:
        next(self._io(dr, set_command_args=str(value).encode(CHARSET)))


class Palette(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"palette"

    def output_cast(self, received_text: str, dr: DygmaRaise) -> ColorPalette:
        return ColorPalette(self._extract_color(received_text))

    def __set__(self, dr: DygmaRaise, value: ColorPalette) -> None:
        next(self._io(dr, set_command_args=value.render_for_command()))


class SettingsCRC(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"settings.crc"

    def output_cast(self,
                    received_text: str,
                    dr: DygmaRaise) -> tuple[int, int]:
        # noinspection PyTypeChecker
        return self._extract_int_tuple(received_text, token="/")

    def __set__(self, instance: DygmaRaise, value: int) -> int:
        raise NotImplementedError


class SettingsDefaultLayer(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"settings.defaultLayer"

    def output_cast(self, received_text: str, dr: DygmaRaise) -> int:
        return int(received_text)

    def __set__(self, dr: DygmaRaise, value: int):
        next(self._io(dr, set_command_args=str(value).encode(CHARSET)))


class SettingsValid(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"settings.valid?"

    def output_cast(self, received_text: str, dr: DygmaRaise) -> bool:
        return self._extract_bool(received_text)


class SettingsVersion(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"settings.version"

    def output_cast(self, received_text: str, dr: DygmaRaise) -> int:
        return int(received_text)

    def __set__(self, instance: DygmaRaise, value: int) -> int:
        raise NotImplementedError


class TapdanceMap(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"tapdance.map"


class Version(DygmaRaiseBaseDescriptor):
    @property
    def command(self) -> bytes:
        return b"version"

    def __get__(self, dr: DygmaRaise, objtype=None) -> VersionType:
        return VersionType(*next(self._io(dr)).split())
