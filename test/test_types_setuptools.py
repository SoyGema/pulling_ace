import unittest
from types_setuptools import *

class TestTypesSetuptools(unittest.TestCase):
    def test_dist(self):
        """Test the Dist type hint."""
        dist = Dist()
        self.assertIsInstance(dist, Dist)

    def test_command(self):
        """Test the Command type hint."""
        command = Command()
        self.assertIsInstance(command, Command)

    def test_requirement(self):
        """Test the Requirement type hint."""
        requirement = Requirement()
        self.assertIsInstance(requirement, Requirement)

    def test_distribution(self):
        """Test the Distribution type hint."""
        distribution = Distribution()
        self.assertIsInstance(distribution, Distribution)

    def test_entry_point(self):
        """Test the EntryPoint type hint."""
        entry_point = EntryPoint()
        self.assertIsInstance(entry_point, EntryPoint)

if __name__ == "__main__":
    unittest.main()
