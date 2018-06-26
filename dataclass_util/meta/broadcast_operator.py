from functools import wraps

from dataclass_util import operator_names


def _unary(op, map):
    @wraps(op)
    def __unary(d):
        return map(op, d)
    return __unary


def _binary(op, map):
    @wraps(op)
    def __binary(d, scalar):
        def _op(el):
            return op(el, scalar)
        return map(_op, d)
    return __binary


def broadcast_operators(map):
    return {
        **{
            name: _unary(op, map)
            for name, op in operator_names.unary.items()
        },
        **{
            name: _binary(op, map)
            for name, op in operator_names.binary.items()
        },
    }
