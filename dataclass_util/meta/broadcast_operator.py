from types import SimpleNamespace
from functools import wraps

from dataclass_util import operator_names


def broadcast_operators(map):
    def unary(op):
        @wraps(op)
        def _unary(d):
            return map(op, d)
        return _unary


    def binary(op):
        @wraps(op)
        def _binary(d, scalar):
            def _op(el):
                return op(el, scalar)
            return map(_op, d)
        return _binary


    return SimpleNamespace(
        **{
            name: unary(op)
            for name, op in operator_names.unary.items()
        },
        **{
            name:  binary(op)
            for name, op in operator_names.binary.items()
        },
    )