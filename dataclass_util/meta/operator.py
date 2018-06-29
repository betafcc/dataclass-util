import builtins
from operator import attrgetter
from types import SimpleNamespace


def make_module(*, replace, asdict=lambda obj: obj.__dict__):
    def map_with_key(f, *objs):
        return replace(objs[0], **{
            k: f(k, *builtins.map(attrgetter(k), objs))
            for k in asdict(objs[0])
        })


    def map(f, *objs):
        return map_with_key(lambda _, *vs: f(*vs), *objs)


    def elementwise(op):
        return lambda *objs: map(op, *objs)


    def broadcast(op):
        return lambda obj, *scalars: map(lambda v: op(v, *scalars), obj)

    return SimpleNamespace(**locals())
