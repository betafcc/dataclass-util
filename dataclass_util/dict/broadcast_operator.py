from dataclass_util.meta import broadcast_operators
from . import map as _map


_locals = locals()
for name, op in broadcast_operators(_map).__dict__.items():
    _locals[name] = op
