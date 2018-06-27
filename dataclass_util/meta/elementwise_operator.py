from types import SimpleNamespace
from functools import wraps


def elementwise_operators(merge_with):
    def binary(op):
        @wraps(op)
        def _binary(da, db, how='left'):
            return merge_with(op, da, db, how=how)
        return _binary

    return SimpleNamespace(**{
        name: binary(op)
        for name, op in operator_names.binary.items()
    })
