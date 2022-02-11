"""
API: https://github.com/Dygmalab/Bazecor/blob/development/FOCUS_API.md
KEY ID MAP: https://github.com/Dygmalab/Raise-Firmware/blob/master/FOCUS_API.MD
reddit: https://www.reddit.com/r/DygmaLab/comments/lsy4y1/api_documentation/
"""


# import copy
import logging


# from auxilary_types import Macro, MacroCode, MacroItem
from dygma_raise import DygmaRaise
# from descriptor import IndexedColor, LedEffect, RGBColor
# from keycodes import KEY_CODES
# from keycodes.key import KeyDefinition, KeyLabel


if __name__ == "__main__":
    # here you can call DygmaRaise.get_serial_ports_with_dygma_raise()
    # to get a tuple of ports connected to a Dygma Raise.
    # The port.device attribute can be passed to the
    # DygmaRaise __new__() / __init__() device= parameter.
    dygma_raise = DygmaRaise(log_level=logging.DEBUG)

    # old_value = dygma_raise.colormap_map
    # new_value = copy.deepcopy(old_value)
    # new_value[0][0] = IndexedColor(1)
    # dygma_raise.colormap_map = new_value
    # input()
    # dygma_raise.colormap_map = old_value

    # old_value = dygma_raise.palette
    # new_value = old_value.copy()
    # new_value[14] = RGBColor(255, 255, 255)
    # dygma_raise.palette = new_value
    # input()
    # dygma_raise.palette = old_value

    # print(dygma_raise.eeprom_contents)
    # print(dygma_raise.eeprom_free)

    # print(dygma_raise.keymap_custom)
    # print(dygma_raise.keymap_default)
    # print(dygma_raise.keymap_only_custom)

    # print(dygma_raise.hardware_crc_errors)
    # print(dygma_raise.hardware_firmware)
    # print(dygma_raise.hardware_joint)
    # print(dygma_raise.hardware_keyscan)
    # print(dygma_raise.hardware_layout)
    # print(dygma_raise.hardware_side_power)
    # print(dygma_raise.hardware_side_ver)
    # print(dygma_raise.hardware_sled_ver)
    # print(dygma_raise.hardware_sled_current)
    # print(dygma_raise.hardware_version)

    print(dygma_raise.help)

    # old_value = dygma_raise.idleleds_time_limit
    # dygma_raise.idleleds_time_limit = 900
    # dygma_raise.idleleds_time_limit = old_value

    # dygma_raise.layer_activate = 4
    # print(dygma_raise.layer_state)

    # noinspection PyUnresolvedReferences
    # old_value = dygma_raise.led_at_0
    # print(old_value)
    # dygma_raise.led_at_0 = RGBColor(0, 0, 0)
    # input()
    # dygma_raise.led_at_0 = old_value

    # old_value = dygma_raise.led_brightness
    # print(old_value)
    # dygma_raise.led_brightness = 30
    # input()
    # dygma_raise.led_brightness = old_value

    # dygma_raise.led_mode = LedEffect.BREATHING
    # input()
    # dygma_raise.led_mode = LedEffect.NORMAL

    # dygma_raise.led_set_all = RGBColor(255, 255, 255)
    # old_value = dygma_raise.led_theme
    # new_value = old_value.copy()
    # new_value[131] = RGBColor(255, 0, 0)
    # dygma_raise.led_theme = new_value
    # input()
    # dygma_raise.led_theme = old_value

    # print(*dygma_raise.macros_map, sep="\n")
    # dygma_raise.macros_map = (
    #     Macro((MacroItem(macro_code=MacroCode.DELAY, value=500),)),
    #     Macro((
    #         MacroItem(
    #             macro_code=MacroCode.KEY_CODE_PRESS_RELEASE,
    #             value=KeyDefinition(
    #                 code=25,
    #                 label=KeyLabel(top='', primary='V', verbose=''))),)))

    # old_value = dygma_raise.palette
    # new_value = old_value.copy()
    # new_value[14] = RGBColor(255, 255, 255)
    # dygma_raise.palette = new_value
    # input()
    # dygma_raise.palette = old_value

    # print(dygma_raise.settings_crc)
    # print(dygma_raise.settings_default_layer)
    # print(dygma_raise.settings_valid)
    # print(dygma_raise.settings_version)

    # print(dygma_raise.superkeys_holdstart)
    # print(dygma_raise.superkeys_map)
    # print(dygma_raise.superkeys_overlap)
    # print(dygma_raise.superkeys_repeat)
    # print(dygma_raise.superkeys_timeout)
    # print(dygma_raise.superkeys_wait_for)

    # print(dygma_raise.tapdance_map)

    # print(dygma_raise.version)

    # print(KEY_CODES)
