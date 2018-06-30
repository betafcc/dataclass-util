from dataclasses import replace, asdict

from .meta.operator import make_module


locals().update(make_module(replace=replace, asdict=asdict).__dict__)


del make_module
