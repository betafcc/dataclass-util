from dataclass_util.meta import elementwise_operators
from . import merge_with


locals().update(elementwise_operators(merge_with).__dict__)


del elementwise_operators
del merge_with
