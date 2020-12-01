import subprocess
from typing import List
from ..objects import Package


def extract_package(line: str) -> Package:
    line = line.split()
    name = line[0].rsplit('/')[0]
    arch = line[2]
    if '-' in line[1]:
        version, patch = line[1].split('-')
    else:
        version = line[1]
        patch = ""
    return Package(name=name, arch=arch, version=version, patch=patch)


def list_packages() -> List[Package]:
    packages = subprocess.run(["apt", "list", "--installed"], stdout=subprocess.PIPE, text=True).stdout.split('\n')[
               1:-1]
    packages = list(map(lambda p: extract_package(p), packages))
    return packages
