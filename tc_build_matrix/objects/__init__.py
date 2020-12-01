from .system import System, LinuxDistribution, Package


class Image:
    def __init__(self, name, system):
        self.name = name
        self.system = system
