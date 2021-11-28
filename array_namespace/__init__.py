from typing import TypeVar, Generic

_StrT = TypeVar("_StrT", bound=str)

__all__: "list[str]" = []


class _NamespaceWrapper(Generic[_StrT]):
    pass


del TypeVar, Generic, _StrT
