from dataclass import replace, asdict

from .meta.operator import make_module


locals().update(make_module(replace=replace, asdict=asdict))


del make_module
