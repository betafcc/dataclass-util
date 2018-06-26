from functools import wraps
from dataclasses import astuple, asdict, replace


import dataclass_util.dataclass


class AsTuple:
    @wraps(astuple)
    def astuple(self):
        return astuple(self)

    def __iter__(self):
        yield from self.astuple()


class AsDict:
    @wraps(asdict)
    def asdict(self):
        return asdict(self)


class Replace:
    @wraps(replace)
    def replace(self, *args, **kwargs):
        return replace(self, *args, **kwargs)


class Map:
    @wraps(dataclass_util.dataclass.map)
    def map(self, f, *args):
        return dataclass_util.dataclass.map(f, self, *args)


# class ElementWiseOperation
