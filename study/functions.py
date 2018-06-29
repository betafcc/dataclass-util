import builtins
from operator import attrgetter
from dataclasses import dataclass, replace, asdict


def map_with_key(f, *objs):
    return replace(objs[0], **{
        k: f(k, *builtins.map(attrgetter(k), objs))
        for k in asdict(objs[0])
    })


def map(f, *objs):
    return map_with_key(lambda _, *vs: f(*vs), *objs)


def elementwise(op):
    return lambda *objs: map(op, *objs)


def broadcast(op):
    return lambda obj, *scalars: map(lambda v: op(v, *scalars), obj)


@dataclass(frozen=True, order=True, eq=True)
class Rectangle:
    x      : int
    y      : int
    width  : int
    height : int




print(elementwise(lambda a, b: a + b)(Rectangle(0, 0, 600, 400), Rectangle(1, 2, 3, 4)))
print(broadcast(lambda a, b, c: (a * b) ** c)(Rectangle(1, 2, 3, 4), 2, 2))
