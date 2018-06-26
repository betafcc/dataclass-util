from typing import Callable, Dict, Set

from functools import reduce
from operator import itemgetter


_map = map


def map(f: Callable, *dicts : Dict) -> Dict:
    common_keys = reduce(_intersection, _map(set, dicts))

    return {
        key: f(*_map(itemgetter(key), dicts))
        for key in common_keys
    }


def _intersection(a : Set, b : Set) -> Set:
    return a.intersection(b)
