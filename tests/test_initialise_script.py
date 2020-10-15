import unittest
from src.constants import member_gender
from initialise_script import initialise_family_tree


class TestInitialiseScript(unittest.TestCase):
    def test_initialise_script_success(self):
        family_tree = initialise_family_tree()
        head_member = family_tree.get_head_member()
        self.assertEqual(head_member.name, 'Shan')
        self.assertEqual(head_member.gender, member_gender['MALE'])


if __name__ == '__main__':
    unittest.main()

