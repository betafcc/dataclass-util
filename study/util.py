from operator import eq, le, lt


# def is_submap_of(a, b):
#     return is_submap_of_by(eq, a, b)


def is_submap_of_by(f, a, b):
    raise NotImplementedError

# def is_proper_submap_of()
# def is_proper_submap_of_by()



assert is_submap_of_by(
    eq,
    from_dict_instance({'a': 1}),
    from_dict_instance({'a': 1, 'b': 2}),
)
assert is_submap_of_by(
    le,
    from_dict_instance({'a': 1}),
    from_dict_instance({'a': 1, 'b': 2}),
)
assert is_submap_of_by(
    eq,
    from_dict_instance({'a': 1, 'b': 2}),
    from_dict_instance({'a': 1, 'b': 2}),
)


assert not is_submap_of_by(
    eq,
    from_dict_instance({'a': 2}),
    from_dict_instance({'a': 1, 'b': 2}),
) 
assert not is_submap_of_by(
    lt,
    from_dict_instance({'a': 1}),
    from_dict_instance({'a': 1, 'b': 2}),
)
assert not is_submap_of_by(
    eq,
    from_dict_instance({'a': 1, 'b': 2}),
    from_dict_instance({'a': 1}),
)

