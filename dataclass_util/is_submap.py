from dataclasses import asdict

from .meta.is_submap import make_module


locals().update(make_module(asdict=asdict).__dict__)


del make_module
