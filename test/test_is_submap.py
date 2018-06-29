from dataclasses import dataclass
from operator import eq, lt, le

import pytest

from dataclass_util.is_submap import is_submap_of_by


@dataclass
class A:
    a : int


@dataclass
class AB:
    a : int
    b : int


# basic tests from examples in
# http://hackage.haskell.org/package/containers-0.6.0.1/docs/Data-Map-Strict.html#g:25
@pytest.mark.parametrize('operator, a, b, expected', [
    (eq, A(a=1),       AB(a=1, b=2), True),
    (le, A(a=1),       AB(a=1, b=2), True),
    (eq, AB(a=1, b=2), AB(a=1, b=2), True),

    (eq, A(a=2),       AB(a=1, b=2), False),
    (lt, A(a=1),       AB(a=1, b=2), False),
    (eq, AB(a=1, b=2), A(a=1),       False),
])
def test_is_submap_of_by(operator, a, b, expected):
    assert is_submap_of_by(operator, a, b) == expected
