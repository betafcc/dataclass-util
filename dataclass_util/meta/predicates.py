from types import SimpleNamespace
from operator import eq


def make_module(*, asdict):
    def is_key_submap(a, b):
        return is_submap_by(lambda _a, _b: True, a, b)


    def is_submap(a, b):
        return is_submap_by(eq, a, b)


    def is_submap_by(f, a, b):
        da, db = asdict(a), asdict(b)

        return all(
            key in db and f(da[key], db[key])
            for key in da
        )


    def has_common_keys(a, b):
        try:
            a, b = asdict(a), asdict(b)
        except TypeError:
            return False

        return any(k in b for k in a)     


    def is_proper_submap(a, b):
        return is_proper_submap_by(eq, a, b)


    def is_proper_submap_by(f, a, b):
        raise NotImplementedError


    return SimpleNamespace(**locals())
