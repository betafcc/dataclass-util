from dataclasses import dataclass
from operator import add, sub, mul

import pytest

from dataclass_util.operator import elementwise


@dataclass
class Point:
    x : int
    y : int


@dataclass
class Rectangle:
    x      : int
    y      : int
    width  : int
    height : int


@pytest.mark.parametrize('operator, a, b, expected', [
    (add, Point(10, 20), Point(1, 2), Point(11, 22)),
    (add, Point(10, 20), Rectangle(1, 2, 3, 4), Point(11, 22)),
    (add, Rectangle(1, 2, 3, 4), Point(10, 20), Rectangle(11, 22, 3, 4)),


    (sub, Point(10, 20), Point(1, 2), Point(9, 18)),
    (sub, Point(10, 20), Rectangle(1, 2, 3, 4), Point(9, 18)),
    (sub, Rectangle(1, 2, 3, 4), Point(10, 20), Rectangle(-9, -18, 3, 4)),


    (mul, Point(10, 20), Point(2, 3), Point(20, 60)),
    (mul, Point(10, 20), Rectangle(2, 3, 4, 5), Point(20, 60)),
    (mul, Rectangle(2, 3, 4, 5), Point(10, 20), Rectangle(20, 60, 4, 5)),
])
def test_elementwise(operator, a, b, expected):
    result = elementwise(operator)(a, b)

    assert result == expected
    assert result != a
    assert result != b


# def test_different_elementwise(operator, a, b, expected):
