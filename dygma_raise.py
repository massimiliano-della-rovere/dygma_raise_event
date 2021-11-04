"""Main class"""


import sys
import logging


from serial.tools.list_ports import comports as list_serial_ports
from serial.tools.list_ports_common import ListPortInfo


from descriptor import (
    ColormapMap,

    EEPROMContents,
    EEPROMFree,

    HardwareCRCErrors,
    HardwareFirmware,
    HardwareJoint,
    HardwareKeyscan,
    HardwareLayout,
    HardwareSidePower,
    HardwareSideVer,
    HardwareSledCurrent,
    HardwareSledVer,
    HardwareVersion,

    Help,

    IdleledsTimeLimit,

    KeymapCustom,
    KeymapDefault,
    KeymapOnlyCustom,

    LedAt,
    LedBrightness,
    LedMode,
    LedSetAll,
    LedTheme,

    MacrosMap,
    MacrosTrigger,

    Palette,

    SettingsCRC,
    SettingsDefaultLayer,
    SettingsValid,
    SettingsVersion,

    TapdanceMap,

    Version,
    VersionType)


# this is port.vid and pairs with port.manufactorer == "Dygma"
DYGMA_VENDOR_ID = 0x1209
# this is port.pid and pairs with port.product == "Raise"
RAISE_PRODUCT_ID = 0x2201


class DygmaRaiseLedAtMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return {
            f"led_at_{i}": LedAt()
            for i in range(132)
        }


class DygmaRaise(metaclass=DygmaRaiseLedAtMeta):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    @staticmethod
    def get_serial_ports_with_dygma_raise() -> tuple[ListPortInfo, ...]:
        return tuple(
            port
            for port in list_serial_ports()
            if port.vid == DYGMA_VENDOR_ID and port.pid == RAISE_PRODUCT_ID)

    def __init__(self, device=None, log_level=logging.INFO):
        if device:
            self._device = device
        else:
            self._device = self.get_serial_ports_with_dygma_raise()[0].device
        self.logger = logging.getLogger("dygma_raise")
        self.logger.setLevel(log_level)
        self.logger.addHandler(logging.StreamHandler(sys.stdout))

    colormap_map = ColormapMap()

    eeprom_contents = EEPROMContents()
    eeprom_free = EEPROMFree()

    hardware_crc_errors = HardwareCRCErrors()
    hardware_firmware = HardwareFirmware()
    hardware_joint = HardwareJoint()
    hardware_keyscan = HardwareKeyscan()
    hardware_layout = HardwareLayout()
    hardware_side_power = HardwareSidePower()
    hardware_side_ver = HardwareSideVer()
    hardware_sled_current = HardwareSledCurrent()
    hardware_sled_ver = HardwareSledVer()
    hardware_version = HardwareVersion()

    help = Help()

    idleleds_time_limit = IdleledsTimeLimit()

    keymap_custom = KeymapCustom()
    keymap_default = KeymapDefault()
    keymap_only_custom = KeymapOnlyCustom()

    # the led_at_* are defined by the DygmaRaiseLedAtMeta metaclass
    led_brightness = LedBrightness()
    led_mode = LedMode()
    led_set_all = LedSetAll()
    led_theme = LedTheme()

    macros_map = MacrosMap()
    macros_trigger = MacrosTrigger()

    palette = Palette()

    settings_crc = SettingsCRC()
    settings_default_layer = SettingsDefaultLayer()
    settings_valid = SettingsValid()
    settings_version = SettingsVersion()

    tapdance_map = TapdanceMap()

    version: VersionType = Version()

    @property
    def device(self) -> str:
        return self._device
