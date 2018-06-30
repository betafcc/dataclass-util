import operator

from dataclass_util.operator import elementwise as _elementwise


def elementwise(cls):
    cls = type(cls.__name__, cls.__bases__, dict(cls.__dict__))

    names = {
        '__add__',
        '__sub__',
        '__mul__',
        '__matmul__',
        '__truediv__',
        '__floordiv__',
        '__mod__',
        # '__divmod__',
        '__pow__',
        '__lshift__',
        '__rshift__',
        '__and__',
        '__xor__',
        '__or__',
    }

    for name in names:
        setattr(cls, name, _elementwise(getattr(operator, name)))

    return cls
