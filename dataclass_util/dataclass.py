from typing import Callable, Any
from dataclasses import asdict, replace

from .dict import map as dmap


_map = map


def map(f     : Callable,
        *objs : Any,
        ) -> Any:

    return replace(objs[0], **dmap(f, *_map(asdict, objs)))
