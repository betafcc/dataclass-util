from builtins import map as _map
from functools import reduce
from operator import itemgetter
from types import SimpleNamespace


def make_module(*, replace, asdict=lambda obj: obj.__dict__, getattr=getattr):
    def map_with_key(f, obj):
        d = asdict(obj)

        return replace(obj, **{
            k: f(k, v)
            for k, v in d.items()
        })


    def map(f, obj):
        return map_with_key(lambda _, v: f(v), obj)


    def merge_by_with_key(f, *objs, how='left'):
        if how == 'left':
            acc = objs[0]
        elif how == 'right':
            acc = objs[-1]
        else:
            raise ValueError(
                f"Methow how='{how}' not supported, use 'left' or 'right'"
            )

        dicts  = list(_map(asdict, objs))
        common = reduce(lambda acc, n: acc.intersection(n), _map(set, dicts))

        return replace(acc, **{
            k: f(k, *_map(itemgetter(k), dicts))
            for k in common
        })


    def merge_by(f, *objs, how='left'):
        return merge_by_with_key(lambda _, *vs: f(*vs), *objs, how=how)


    def elementwise(op, how='left'):
        return lambda *objs: merge_by(op, *objs, how=how)


    def broadcast(op):
        return lambda obj, *scalars: map(lambda v: op(v, *scalars), obj)

    return SimpleNamespace(**locals())
