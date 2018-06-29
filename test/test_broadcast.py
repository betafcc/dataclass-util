from dataclasses import dataclass
from operator import add, sub, mul, truediv

import pytest

from dataclass_util.operator import broadcast


@dataclass
class Rectangle:
    x      : int
    y      : int
    width  : int
    height : int


@pytest.mark.parametrize('operator, a, b, expected', [
    (add, Rectangle(10, 20, 300, 400), 1, Rectangle(11, 21, 301, 401)),
    (sub, Rectangle(10, 20, 300, 400), 1, Rectangle(9, 19, 299, 399)),
    (mul, Rectangle(10, 20, 300, 400), 2, Rectangle(20, 40, 600, 800)),
    (truediv, Rectangle(10, 20, 300, 400), 2, Rectangle(5, 10, 150, 200)),
])
def test_broadcast(operator, a, b, expected):
    result = broadcast(operator)(a, b)

    assert result == expected
    assert result != a
    assert result != b
