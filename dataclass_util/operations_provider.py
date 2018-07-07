import operator
from collections.abc import Iterable


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


def operations_provider(operator_wrapper):

    def set_operations(fields=None,
                       *,
                       on=lambda self, other: True,
                       include=operations,
                       exclude=frozenset()
                       ):
        _fields = None
        if isinstance(fields, str):
            _fields = set(fields.split())
        elif isinstance(fields, Iterable):
            _fields = set(fields)

        def _set_operations(cls):
            # Copy the class, don't wanna modify the original
            cls = type(cls.__name__, cls.__bases__, dict(cls.__dict__))

            # Sets the selected methods
            for op_name in set(include) - set(exclude):
                new_method = if_(condition=on,
                                 on_true=operator_wrapper(getattr(operator, op_name), keys=_fields),
                                 # fallback to current method on 'cls'
                                 on_false=getattr(cls, op_name, not_implemented(op_name)),
                                 )

                setattr(cls, op_name, new_method)

            return cls

        # if used as decorator without arguments
        if callable(fields):
            return _set_operations(fields)
        return _set_operations

    return set_operations


def if_(condition, on_true, on_false):
    def _if_(*args, **kwargs):
        if condition(*args, **kwargs):
            return on_true(*args, **kwargs)
        else:
            return on_false(*args, **kwargs)
    return _if_


def not_implemented(name):
    def _not_implemented(self, other):
        raise TypeError(
            f"'{name}' not implemented for " +
            f"'{type(self).__name__}' and '{type(other).__name__}'"
        )
    return _not_implemented
