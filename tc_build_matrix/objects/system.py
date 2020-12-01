from .package import Package
from .linux_distribution import LinuxDistribution
from typing import List


class System:
    def __init__(self, distribution: LinuxDistribution, packages: List[Package]):
        self.distribution = distribution
        self.packages = packages
