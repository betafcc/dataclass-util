import operator
from dataclasses import dataclass, asdict

import dataclass_util.operator as wrapper 
from dataclass_util.predicates import has_common_keys
from dataclass_util.operations_provider import operations_provider


elementwise = operations_provider(wrapper.elementwise)
broadcast   = operations_provider(wrapper.broadcast)


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
