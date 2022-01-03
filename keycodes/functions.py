"""function to combine keycodes with modifier codes."""


import enum
import itertools
import typing


from .key import KeyDefinition, KeyGroup, KeyLabel


class ModifierBitMask(enum.IntEnum):
    CTRL = 256
    ALT = 512
    ALT_GR = 1024
    SHIFT = 2024
    GUI = 4096


class ModifierInfo(typing.NamedTuple):
    group_name: str
    label_top: str
    bit_mask: int | ModifierBitMask


MODIFIERS = (
    ModifierInfo(
        group_name="Control +",
        label_top="C+",
        bit_mask=ModifierBitMask.CTRL),
    ModifierInfo(
        group_name="Alt +",
        label_top="A+",
        bit_mask=ModifierBitMask.ALT),
    ModifierInfo(
        group_name="AltGr +",
        label_top="AGr+",
        bit_mask=ModifierBitMask.ALT_GR),
    ModifierInfo(
        group_name="Shift +",
        label_top="S+",
        bit_mask=ModifierBitMask.SHIFT),
    ModifierInfo(
        group_name="Gui +",
        label_top="G+",
        bit_mask=ModifierBitMask.GUI))


T = typing.TypeVar("T")


def modifiers_powerset(iterable: typing.Iterable[T]) \
        -> typing.Iterable[typing.Sequence[T]]:
    """powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"""
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1))


def merge_modifiers(powerset: typing.Iterable[typing.Sequence[ModifierInfo]]) \
        -> typing.Generator[ModifierInfo, None, None]:
    for set_of_modifiers in powerset:
        group_name = []
        label_top = []
        bit_mask = 0
        for modifier in set_of_modifiers:
            group_name.append(modifier.group_name)
            label_top.append(modifier.label_top)
            bit_mask |= modifier.bit_mask
        yield ModifierInfo(
            group_name=" ".join(group_name),
            label_top=" ".join(label_top),
            bit_mask=bit_mask)


MODIFIERS_POWERSET = tuple(merge_modifiers(modifiers_powerset(MODIFIERS)))


def with_modifiers(key_group: KeyGroup,
                   group_name: str,
                   label_top: str,
                   bit_mask: int | ModifierBitMask) -> KeyGroup:
    """
    porting of
    https://github.com/Dygmalab/Bazecor/blob/development/src/api/keymap/db/utils.js
    """
    return KeyGroup(
        name=key_group.name,
        keys=tuple(
            KeyDefinition(
                code=key.code + bit_mask,
                label=KeyLabel(
                    top=f"{label_top} {key.label.top}".strip(),
                    primary=key.label.primary,
                    verbose=""))
            for key in key_group.keys))
