"""Main class"""


import sys
import logging


from descriptor import (
    ColormapMap,

    EEPROMContents,
    EEPROMFree,

    HardwareJoint,
    HardwareLayout,

    IdleledsTimeLimit,

    KeymapCustom,
    KeymapDefault,
    KeymapOnlyCustom,

    LedAt,
    LedBrightness,
    LedMode,
    LedSetAll,
    LedTheme,

    Palette,

    SettingsCRC,
    SettingsDefaultLayer,
    SettingsValid,
    SettingsVersion,
    Version, VersionType)


class DygmaRaiseLedAtMeta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return {
            f"led_at_{i}": LedAt()
            for i in range(132)
        }


class DygmaRaise(metaclass=DygmaRaiseLedAtMeta):
    def __new__(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    def __init__(self, device="/dev/ttyACM0", log_level=logging.INFO):
        self._device = device
        self.logger = logging.getLogger("dygma_raise")
        self.logger.setLevel(log_level)
        self.logger.addHandler(logging.StreamHandler(sys.stdout))

    colormap_map = ColormapMap()

    eeprom_contents = EEPROMContents()
    eeprom_free = EEPROMFree()

    hardware_joint = HardwareJoint()
    hardware_layout = HardwareLayout()

    idleleds_time_limit = IdleledsTimeLimit()

    keymap_custom = KeymapCustom()
    keymap_default = KeymapDefault()
    keymap_only_custom = KeymapOnlyCustom()

    # the led_at_* are defined by the DygmaRaiseLedAtMeta metaclass
    led_brightness = LedBrightness()
    led_mode = LedMode()
    led_set_all = LedSetAll()
    led_theme = LedTheme()

    palette = Palette()

    settings_crc = SettingsCRC()
    settings_default_layer = SettingsDefaultLayer()
    settings_valid = SettingsValid()
    settings_version = SettingsVersion()

    version: VersionType = Version()

    @property
    def device(self) -> str:
        return self._device
