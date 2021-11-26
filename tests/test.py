import sys

import pytest
import array_namespace

if sys.version_info >= (3, 8):
    from typing import Literal as L
else:
    from typing_extensions import Literal as L


@pytest.mark.parametrize("name", array_namespace.__all__)
def test_all(name: str) -> None:
    assert hasattr(array_namespace, name)


def test_generic() -> None:
    assert array_namespace.NamespaceWrapper[str]
    assert array_namespace.NamespaceWrapper[L["array_namespace"]]
