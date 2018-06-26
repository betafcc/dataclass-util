from functools import wraps

from . import broadcast
from . import map as dmap
from dataclass_util import operator_names


def _unary(op):
    @wraps(op)
    def __unary(d):
        return dmap(op, d)
    return __unary


for name, op in operator_names.unary.items():
    locals()[name] = _unary(op)


def _binary(op):
    @wraps(op)
    def __binary(d, scalar):
        def _op(el):
            return op(el, scalar)
        return dmap(_op, d)
    return __binary


for name, op in operator_names.binary.items():
    locals()[name] = _binary(op)
