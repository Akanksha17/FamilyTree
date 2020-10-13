import unittest
from initialise_script import initialise_family_tree


class TestInitialiseScript(unittest.TestCase):
    def test_initialise_script_success(self):
        family_tree = initialise_family_tree()
        print(family_tree.members)


if __name__ == '__main__':
    unittest.main()

