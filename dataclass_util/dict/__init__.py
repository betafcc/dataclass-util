from typing import Callable, Dict, Set, Any

from functools import reduce
from operator import itemgetter


_map = map


def map(f : Callable,
        *dicts : Dict,
        ) -> Dict:
    common_keys = reduce(
        lambda acc, n: acc.intersection(n),
        _map(set, dicts),
    )

    return {
        key: f(*_map(itemgetter(key), dicts))
        for key in common_keys
    }


def merge_with(f   : Callable,
               a   : Dict,
               b   : Dict,
               how : str = 'inner',
               ) -> Dict:
    if how == 'left':
        acc = a
    elif how == 'right':
        acc = b
    elif how == 'outer':
        acc = {**a, **b}
    elif how == 'inner':
        acc = {}
    else:
        raise ValueError(f"'{how}' not valid merge method for dicts")

    return {**acc, **map(f, a, b)}


def broadcast(op     : Callable,
              d      : Dict,
              scalar : Any,
              ) -> Dict:
    return map(lambda el: op(el, scalar), d)
