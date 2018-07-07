import operator
from dataclasses import dataclass, asdict

from dataclass_util.class_ import elementwise, broadcast


@elementwise(on=has_common_keys)
@broadcast
@dataclass(frozen=True, eq=True, order=True)
class Rectangle:
    x      : int
    y      : int
    width  : int
    height : int


@dataclass
class Point:
    x : int
    y : int


print(
    Rectangle(1, 2, 400, 600)
    *
    Point(10, 20)
)

print(
    Rectangle(1, 2, 400, 600)
    *
    2
)
