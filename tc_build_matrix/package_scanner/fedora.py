import subprocess
from typing import List
from ..objects import Package


def extract_package(line: str) -> Package:
    line = line.split()
    name, arch = line[0].rsplit('.', 1)
    version, patch = line[1].split('-')
    patch = patch.split('.')[0]
    return Package(name=name, arch=arch, version=version, patch=patch)


def list_packages() -> List[Package]:
    packages = subprocess.run(["dnf", "list", "installed"], stdout=subprocess.PIPE, text=True).stdout.split('\n')[1:-1]
    packages = list(map(lambda p: extract_package(p), packages))
    return packages
