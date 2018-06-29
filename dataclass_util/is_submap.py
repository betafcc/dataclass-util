from dataclasses import asdict

from .meta.is_submap import make_module


locals().update(make_module(asdict=asdict, getattr=getattr).__dict__)


del make_module
