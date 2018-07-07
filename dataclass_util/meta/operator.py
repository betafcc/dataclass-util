from functools import reduce
from types import SimpleNamespace


def make_module(*, replace, asdict=lambda obj: obj.__dict__):
    def map_with_key(f, obj):
        d = asdict(obj)

        return replace(obj, **{
            k: f(k, v)
            for k, v in d.items()
        })


    def map(f, obj):
        return map_with_key(lambda _, v: f(v), obj)


    def merge_with_key_by(f, *objs, how='left'):
        if how == 'left':
            acc = objs[0]
        elif how == 'right':
            acc = objs[-1]
        else:
            raise ValueError(
                f"Methow how='{how}' not supported, use 'left' or 'right'"
            )

        dicts  = [asdict(obj) for obj in objs]
        common = reduce(lambda acc, n: acc.intersection(n), (set(d) for d in dicts))

        return replace(acc, **{
            k: f(k, *(d[k] for d in dicts))
            for k in common
        })


    def merge_by(f, *objs, how='left'):
        return merge_with_key_by(lambda _, *vs: f(*vs), *objs, how=how)


    def elementwise(op, keys=None, how='left'):
        if keys is None:
            return lambda *objs: merge_by(op, *objs, how=how)

        return lambda *objs: merge_with_key_by(
            lambda k, a, b: op(a, b) if k in keys else a,
            *objs,
            how=how,
        )


    def broadcast(op, keys=None):
        if keys is None:
            return lambda obj, *scalars: map(lambda v: op(v, *scalars), obj)

        return lambda obj, *scalars: map_with_key(
            lambda k, v: op(v, *scalars) if k in keys else v,
            obj,
        )


    return SimpleNamespace(**locals())
