from ..distribution_info import linux_distribution_name
from . import fedora, ubuntu

__LIST_PACKAGES__ = {
    'fedora': fedora.list_packages,
    'ubuntu': ubuntu.list_packages,
    'debian': ubuntu.list_packages
}


def list_packages():
    return __LIST_PACKAGES__.get(linux_distribution_name(), lambda: [])()
