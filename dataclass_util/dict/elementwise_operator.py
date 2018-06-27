from dataclass_util.dict.elementwise_operator import elementwise_operators
from . import _merge_with


_locals = locals()
for name, op in elementwise_operators(merge_with).__dict__.items():
    _locals[name] = op
