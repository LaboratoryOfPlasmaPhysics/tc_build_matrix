import unittest
from tc_build_matrix.package_scanner import list_packages


class TestListPackage(unittest.TestCase):
    def test_should_get_at_least_few_packages(self):
        packages = list_packages()
        self.assertGreater(len(packages), 1)

