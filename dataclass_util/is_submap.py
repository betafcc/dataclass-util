from operator import eq
from dataclasses import asdict


def is_key_submap_of(a, b):
    return is_submap_of_by(lambda _a, _b: True, a, b)


def is_submap_of(a, b):
    return is_submap_of_by(eq, a, b)


def is_submap_of_by(f, a, b):
    for k, v in asdict(a).items():
        try:
            if not f(getattr(b, k), v):
                return False
        except AttributeError:
            return False

    return True


def is_proper_submap_of(a, b):
    return is_proper_submap_of_by(eq, a, b)


def is_proper_submap_of_by(f, a, b):
    raise NotImplementedError
