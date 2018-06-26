import operator


unary = [
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

unary = {
    name: getattr(operator, name)
    for name in unary
}


binary = [
    'lt',
    'le',
    'eq',
    'ne',
    'ge',
    'gt',
    '__lt__',
    '__le__',
    '__eq__',
    '__ne__',
    '__ge__',
    '__gt__',
    'add',
    '__add__',
    'and_',
    '__and__',
    'floordiv',
    '__floordiv__',
    'lshift',
    '__lshift__',
    'mod',
    '__mod__',
    'mul',
    '__mul__',
    'matmul',
    '__matmul__',
    'or_',
    '__or__',
    'pow',
    '__pow__',
    'rshift',
    '__rshift__',
    'sub',
    '__sub__',
    'truediv',
    '__truediv__',
    'xor',
    '__xor__',
    'concat',
    '__concat__',
    'contains',
    '__contains__',
    'countOf',
    'delitem',
    '__delitem__',
    'getitem',
    '__getitem__',
    'indexOf',
]

binary = {
    name: getattr(operator, name)
    for name in binary
}
