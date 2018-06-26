import operator

from . import broadcast
from . import map as dmap


_unary = [
    'not_',
    '__not__',
    'truth',
    'is_',
    'is_not',
    'abs',
    '__abs__',
    'index',
    '__index__',
    'inv',
    'invert',
    '__inv__',
    '__invert__',
    'pos',
    '__pos__',
    'neg',
    '__neg__',
]


for op in _unary:
    exec(f'def {op}(d): return dmap(operator.{op}, d)')


# operator.lt(a, b)
# operator.le(a, b)
# operator.eq(a, b)
# operator.ne(a, b)
# operator.ge(a, b)
# operator.gt(a, b)
# operator.__lt__(a, b)
# operator.__le__(a, b)
# operator.__eq__(a, b)
# operator.__ne__(a, b)
# operator.__ge__(a, b)
# operator.__gt__(a, b)
# operator.add(a, b)
# operator.__add__(a, b)
# operator.and_(a, b)
# operator.__and__(a, b)
# operator.floordiv(a, b)
# operator.__floordiv__(a, b)
# operator.lshift(a, b)
# operator.__lshift__(a, b)
# operator.mod(a, b)
# operator.__mod__(a, b)
# operator.mul(a, b)
# operator.__mul__(a, b)
# operator.matmul(a, b)
# operator.__matmul__(a, b)
# operator.or_(a, b)
# operator.__or__(a, b)
# operator.pow(a, b)
# operator.__pow__(a, b)
# operator.rshift(a, b)
# operator.__rshift__(a, b)
# operator.sub(a, b)
# operator.__sub__(a, b)
# operator.truediv(a, b)
# operator.__truediv__(a, b)
# operator.xor(a, b)
# operator.__xor__(a, b)
# operator.concat(a, b)
# operator.__concat__(a, b)
# operator.contains(a, b)
# operator.__contains__(a, b)
# operator.countOf(a, b)
# operator.delitem(a, b)
# operator.__delitem__(a, b)
# operator.getitem(a, b)
# operator.__getitem__(a, b)
# operator.indexOf(a, b)

# operator.setitem(a, b, c)
# operator.__setitem__(a, b, c)
