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


def operations_provider(operator_decorator):

    def class_decorator(fields=None,
                        *,
                        on=lambda self, other: True,
                        include=operations,
                        exclude=frozenset()
                        ):
        def _class_decorator(cls):
            # Copy the class, don't wanna modify the original
            cls = type(cls.__name__, cls.__bases__, dict(cls.__dict__))

            # Sets the selected methods
            for op_name in set(include) - set(exclude):
                # Decorates the operation from stdlib operator module
                main     = operator_decorator(getattr(operator, op_name))
                # Fallback to be existing implementation of current 'op_name' in 'cls'
                fallback = getattr(cls, op_name, default_exception(op_name))

                method = if_(cond=on,
                             on_true=main,
                             on_false=fallback,
                             )

                setattr(cls, op_name, method)

            return cls

        # if used as decorator without arguments
        if callable(fields):
            return _class_decorator(fields)
        return _class_decorator

    return class_decorator


broadcast   = operations_provider(wrap.broadcast)
elementwise = operations_provider(wrap.elementwise)


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
