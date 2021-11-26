from typing import TypeVar, Generic

_StrT = TypeVar("_StrT", bound=str)

__all__ = ["NamespaceWrapper"]


class NamespaceWrapper(Generic[_StrT]):
    pass
