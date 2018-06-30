from dataclasses import dataclass
from operator import eq, lt, le

import pytest

from dataclass_util.is_submap import is_submap_by


@dataclass
class A:
    a : int


@dataclass
class AB:
    a : int
    b : int


@dataclass
class C:
    c : int


# basic tests from examples in
# http://hackage.haskell.org/package/containers-0.6.0.1/docs/Data-Map-Strict.html#g:25
@pytest.mark.parametrize('operator, a, b, expected', [
    (eq, A(a=1),       AB(a=1, b=2), True),
    (le, A(a=1),       AB(a=1, b=2), True),
    (eq, AB(a=1, b=2), AB(a=1, b=2), True),

    (eq, A(a=2),       AB(a=1, b=2), False),
    (lt, A(a=1),       AB(a=1, b=2), False),
    (eq, AB(a=1, b=2), A(a=1),       False),

    (eq, C(c=1), AB(a=1, b=2), False),
])
def test_is_submap_by(operator, a, b, expected):
    assert is_submap_by(operator, a, b) == expected


# @pytest.mark.parametrize('operator, a, b, expected', [
#     (eq, , , True),
#     (le, , , True),

#     (eq, , , False),
#     (eq, , , False),
#     (lt, , , False),
# ])
# def test_is_proper_submap_by(operator, a, b, expected):
#     assert test_is_proper_submap_by(operator, a, b) == expected
