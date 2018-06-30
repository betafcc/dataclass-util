from types import SimpleNamespace


def make_module(*, replace, asdict=lambda obj: obj.__dict__, getattr=getattr):
    def map_with_key(f, *objs):
        return replace(objs[0], **{
            k: f(k, *(getattr(obj, k) for obj in objs))
            for k in asdict(objs[0])
        })


    def map(f, *objs):
        return map_with_key(lambda _, *vs: f(*vs), *objs)


    def merge_with(f, *objs, how='left'):
        raise NotImplementedError


    def elementwise(op, how='left'):
        return lambda *objs: merge_with(op, *objs, how=how)


    def broadcast(op):
        return lambda obj, *scalars: map(lambda v: op(v, *scalars), obj)

    return SimpleNamespace(**locals())
