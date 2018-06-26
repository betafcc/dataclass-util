from functools import wraps

from . import broadcast
from . import map as dmap
from . import operator_names


_locals = locals()

for name, op in operator_names.unary.items():
    _locals[name] = wraps(op)(lambda d: dmap(op, d))
