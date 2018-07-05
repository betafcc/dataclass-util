import operator

import dataclass_util.operator as wrap


operations = frozenset({
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
})


def elementwise(fields=None,
                *,
                on=lambda self, other: True,
                include=operations,
                exclude=frozenset(),
                ):
    def _elementwise(cls):
        cls = type(cls.__name__, cls.__bases__, dict(cls.__dict__))

        for op_name in set(include) - set(exclude):
            try:
                fallback = getattr(cls, op_name)
            except AttributeError:
                fallback = default_exception(op_name)

            f = if_(cond=on,
                    on_true=wrap.elementwise(getattr(operator, op_name)),
                    on_false=fallback,
                    )

            setattr(cls, op_name, f)

        return cls

    # if used as decorator without arguments
    if callable(fields):
        return _elementwise(fields)
    return _elementwise


def if_(cond, on_true, on_false):
    def _if_(*args, **kwargs):
        if cond(*args, **kwargs):
            return on_true(*args, **kwargs)
        else:
            return on_false(*args, **kwargs)
    return _if_


def default_exception(name):
    def _default_exception(self, other):
        raise TypeError(
            f"'{name}' not implemented for " +
            f"'{type(self).__name__}' and '{type(other).__name__}'"
        )
    return _default_exception
