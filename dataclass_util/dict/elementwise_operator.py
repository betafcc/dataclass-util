from dataclass_util.meta import elementwise_operators
from . import merge_with as _merge_with


_locals = locals()
for name, op in elementwise_operators(_merge_with).__dict__.items():
    _locals[name] = op
