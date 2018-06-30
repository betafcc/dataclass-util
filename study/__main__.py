import operator
from dataclasses import dataclass

from dataclass_util.operator import elementwise


# def elementwise(fields, on, methods):
#     def _elementwise(cls):
#         return cls
#     return _elementwise


# @elementwise(
#     fields=['x', 'y'],
#     on=lambda self, other: is_submap(self, other),
#     methods=['__add__', '__sub__', '__mul__'],
# )


def elementwisefy(cls):
    cls = type(cls.__name__, cls.__bases__, dict(cls.__dict__))

    for op in ['add', 'sub', 'mul', 'truediv', 'floordiv', 'matmul', 'pow']:
        op = f'__{op}__'
        setattr(cls, op, elementwise(getattr(operator, op)))

    return cls


@elementwisefy
@dataclass(frozen=True, eq=True, order=True)
class Rectangle:
    x      : int
    y      : int
    width  : int
    height : int


ERectangle = elementwisefy(Rectangle)


print(
    ERectangle(1, 2, 400, 600)
    +
    ERectangle(3, 5, 100, 200)
)
