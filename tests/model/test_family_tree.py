import unittest
from src.models import family_tree as family_tree_model, member as member_model
from src.constants import member_gender


class TestFamilyTree(unittest.TestCase):
    def test_family_tree_init(self):
        member = member_model.Member('Sherlock', member_gender['MALE'])
        members = {
                'Sherlock': member
            }
        family_tree = family_tree_model.FamilyTree(members)
        self.assertEqual(family_tree.members['Sherlock'], member)

    def test_family_tree_head(self):
        member = member_model.Member('Sherlock', member_gender['MALE'])
        family_tree = family_tree_model.FamilyTree()
        family_tree.set_head_member(member)
        self.assertEqual(family_tree.get_head_member(), member)
