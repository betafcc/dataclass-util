from dataclasses import dataclass
from operator import add, sub, mul

import pytest

import dataclass_util.operator as wrapper
from dataclass_util.operations_provider import operations_provider


elementwise = operations_provider(wrapper.elementwise)
broadcast   = operations_provider(wrapper.broadcast)


@elementwise
@dataclass
class Point:
    x : int
    y : int


@elementwise
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
    result = operator(a, b)

    assert result == expected
    assert result != a
    assert result != b


def test_selected_fields():
    @elementwise('x y')
    @dataclass
    class NamedPoint:
        name : str
        x    : int
        y    : int

    origin = NamedPoint('origin', 0, 0)
    home   = NamedPoint('home', 320, 910)

    assert home + origin == home


    assert home + Point(11, 22) == NamedPoint('home', 331, 932)
    assert Point(11, 22) + home == Point(331, 932)


    @broadcast('x y')
    @dataclass
    class NamedPoint:
        name : str
        x    : int
        y    : int

    assert NamedPoint('foo', 2, 3) ** 2 == NamedPoint('foo', 4, 9)
