import unittest
from src.service import family_tree as family_tree_service
from src.models import member as member_model, family_tree as family_tree_model
from src.constants import member_gender, output_messages


class TestFamilyTree(unittest.TestCase):
    def test_family_tree_update(self):
        command = 'ADD_CHILD Shan Chit Male'
        new_member = member_model.Member('Shan', member_gender['Male'])
        members_obj = {
            'Shan': new_member
        }
        family_tree_obj = family_tree_model.FamilyTree(members_obj)
        family_tree_obj.set_head_member(new_member)
        result = family_tree_service.update_family_tree(family_tree_obj, command)
        self.assertEqual(result['msg'], output_messages['CHILD_ADDITION_SUCCEEDED'])
        newly_created_child = result['updated_family_tree'].members['Chit']
        self.assertEqual(newly_created_child.get_parent(), new_member)


if __name__ == '__main__':
    unittest.main()