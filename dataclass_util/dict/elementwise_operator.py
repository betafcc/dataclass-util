from functools import wraps

from . import merge_with
from . import operator_names


def _binary(op):
    @wraps(op)
    def __binary(da, db, how='left'):
        return merge_with(op, da, db, how=how)
    return __binary


for name, op in operator_names.binary.items():
    locals()[name] = _binary(op)
