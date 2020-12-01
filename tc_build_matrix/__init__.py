"""Top-level package for Teamcity build matrix helper."""

__author__ = """Alexis Jeandet"""
__email__ = 'alexis.jeandet@member.fsf.org'
__version__ = '0.1.0'

from .objects import LinuxDistribution, System, Image
from .package_scanner import list_packages
from .distribution_info import linux_distribution


def scan(name):
    return Image(
        name=name,
        system=System(linux_distribution(), list_packages())
    )
