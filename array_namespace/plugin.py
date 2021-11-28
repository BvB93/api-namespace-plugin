import sys

import mypy.types
from mypy.types import Type, UnboundType
from mypy.plugin import Plugin, AnalyzeTypeContext
from mypy.nodes import MypyFile, ImportFrom, Statement

if sys.version_info >= (3, 9):
    from typing import Callable
else:
    from collections.abc import Callable

__all__ = ["plugin"]


def _type_analyze_hook(ctx: AnalyzeTypeContext) -> Type:
    """Replace a type-alias with a concrete ``NBitBase`` subclass."""
    typ, _, api = ctx

    try:
        marker = typ.args[1].args[0].name
        module = typ.args[2].args[0].name
        assert marker == "__array_namespace__"
        assert isinstance(module, str)
    except Exception:
        return typ

    import pdb; pdb.set_trace()
    ret = api.named_type("array_namespace._NamespaceProxy")


class _NamespacePlugin(Plugin):
    """A mypy plugin for handling versus numpy-specific typing tasks."""

    def get_method_hook(self, fullname: str) -> "None | Callable[[AnalyzeTypeContext], Type]":
        """Set the precision of platform-specific `numpy.number`
        subclasses.

        For example: `numpy.int_`, `numpy.longlong` and `numpy.longdouble`.
        """
        if fullname.endswith("__array_namespace__"):
            return _type_analyze_hook
        return None


def plugin(version: str) -> "type[_NamespacePlugin]":
    """An entry-point for mypy."""
    return _NamespacePlugin
