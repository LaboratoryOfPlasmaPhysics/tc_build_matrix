from yaml import dump as yaml_dump
from yaml import load as yaml_load
from typing import Dict, Union, List
from functools import singledispatch
from ..objects import Package, LinuxDistribution, System, Image


@singledispatch
def to_dict(obj):
    pass


@to_dict.register(Package)
def _(package):
    return package.__dict__


@to_dict.register(list)
def _(objects):
    return [to_dict(obj) for obj in objects]


@to_dict.register(LinuxDistribution)
def _(distrib):
    return distrib.__dict__


@to_dict.register(System)
def _(system):
    return {
        'distribution': to_dict(system.distribution),
        'packages': to_dict(system.packages)
    }


@to_dict.register(Image)
def _(image):
    return {
        'name': image.name,
        'system': to_dict(image.system)
    }


@singledispatch
def from_dict(d: dict) -> Image:
    return Image(name=d['name'],
                 system=System(
                     distribution=LinuxDistribution(**d['system']['distribution']),
                     packages=
                     [
                         Package(**p) for p in d['system']['packages']
                     ]
                 )
                 )


@singledispatch
def to_yaml(data) -> Union[str, bytes]:
    return yaml_dump(to_dict(data))


@to_yaml.register(dict)
def _(data):
    return yaml_dump(data)


def from_yaml(data: Union[str, bytes]) -> Image:
    return from_dict(yaml_load(data))
