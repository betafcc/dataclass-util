from types import ModuleType
from functools import wraps

from dataclass_util import operator_names


def elementwise_operators(merge_with, name='elementwise_operator', doc=None):
    def binary(op):
        @wraps(op)
        def _binary(da, db, how='left'):
            return merge_with(op, da, db, how=how)
        return _binary


    module = ModuleType(name, doc=doc)
    for name, op in operator_names.binary.items():
        setattr(module, name, op)

    return module


def broadcast_operators(map, name='broadcast_operator', doc=None):
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


    module = ModuleType(name, doc=doc)
    for name, op in [*operator_names.unary.items(), *operator_names.binary.items()]:
        setattr(module, name, op)

    return module
