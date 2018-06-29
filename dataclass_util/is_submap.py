from operator import eq


def is_submap_of(a, b):
    return is_submap_of_by(eq, a, b)


def is_submap_of_by(f, a, b):
    raise NotImplementedError


def is_proper_submap_of(a, b):
    return is_proper_submap_of_by(eq, a, b)


def is_proper_submap_of_by(f, a, b):
    raise NotImplementedError
