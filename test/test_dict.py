from dataclass_util.dict import map as dmap



def test_dmap():
    a = {'a': 1, 'b': 2, 'c': 3}

    assert dmap(lambda x: x**2, a) == {'a': 1, 'b': 4, 'c': 9}


def test_variadic_dmap():
    to_tuple = lambda *args: tuple(args)
    assert dmap(to_tuple, {'a': 1}, {'a': 2}, {'a': 3}) == {'a': (1, 2, 3)}
