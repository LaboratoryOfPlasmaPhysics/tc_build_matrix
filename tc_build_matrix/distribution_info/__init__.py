import os
from functools import cache
from ..objects import LinuxDistribution


@cache
def linux_distribution():
    if os.path.exists('/etc/os-release'):
        with open('/etc/os-release', 'r') as rel_file:
            lines = rel_file.readlines()
            mapped = {
                key: value.removesuffix('\n') for key, value in map(lambda l: l.split('='), lines)
            }
            return LinuxDistribution(mapped["ID"], mapped["VERSION_ID"])


@cache
def linux_distribution_name():
    return linux_distribution().name
