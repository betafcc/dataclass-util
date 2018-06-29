from types import SimpleNamespace
from operator import eq


def make_module(*, asdict, getattr=getattr):
    def is_key_submap(a, b):
        return is_submap_by(lambda _a, _b: True, a, b)


    def is_submap(a, b):
        return is_submap_by(eq, a, b)


    def is_submap_by(f, a, b):
        for k, v in asdict(a).items():
            try:
                if not f(getattr(b, k), v):
                    return False
            except AttributeError:
                return False

        return True


    def is_proper_submap(a, b):
        return is_proper_submap_by(eq, a, b)


    def is_proper_submap_by(f, a, b):
        raise NotImplementedError


    return SimpleNamespace(**locals())
