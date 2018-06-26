from typing import Callable, Any, Dict
from dataclasses import asdict, replace

from dataclass_util.dict import map as dict_map


_map = map


def map(f     : Callable,
        *objs : Any,
        ) -> Any:

    return replace(objs[0], **dict_map(f, *_map(asdict, objs)))


def merge_with(f   : Callable,
               a   : Any,
               b   : Any,
               how : str = 'left',
               ) -> Any:
    if how == 'left':
        return map(f, a, b)
    elif how == 'right':
        return map(lambda _b, _a: f(_a, _b), b, a)

    raise ValueError(f"'{how}' not valid merge method for dataclasses")


def broadcast(op     : Callable,
              d      : Any,
              scalar : Any,
              ) -> Dict:
    return map(lambda el: op(el, scalar), d)
