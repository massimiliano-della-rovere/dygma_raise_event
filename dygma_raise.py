"""Main class"""


import sys
import logging


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

    def __init__(self, device="/dev/ttyACM0", log_level=logging.INFO):
        self._device = device
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
