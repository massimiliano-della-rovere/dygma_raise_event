import typing


class KeyLabel(typing.NamedTuple):
    top: typing.Optional[str]
    primary: typing.Optional[str]
    verbose: typing.Optional[str]


class KeyDefinition(typing.NamedTuple):
    code: int
    label: KeyLabel


class KeyGroup(typing.NamedTuple):
    name: str
    keys: tuple[KeyDefinition, ...]
