from src.action import member as member_action
from src.models import member as member_model, family_tree as family_tree_model
from src.constants import valid_actions, member_gender, output_messages
import unittest

child_action = valid_actions['ADD_CHILD']
get_relationship_action = valid_actions['GET_RELATIONSHIP']

first_member = member_model.Member('Anga', member_gender['FEMALE'])
members_obj = {
    'Anga': first_member
}

family_tree_obj = family_tree_model.FamilyTree(members_obj)
family_tree_obj.set_head_member(first_member)


class TestMemberAction(unittest.TestCase):
    def test_add_child_action_success(self):
        result = member_action.execute(child_action, family_tree_obj, ['Anga', 'Chit', 'Male'])
        self.assertEqual(result['success_msg'], output_messages['CHILD_ADDITION_SUCCEEDED'])
        newly_added_member = result['updated_family_tree'].members['Chit']
        parent = newly_added_member.get_parent()
        self.assertEqual(parent, first_member)

    def test_get_relationship_action_success(self):
        member_action.execute(child_action, family_tree_obj, ['Anga', 'Chit', 'Male'])
        result = member_action.execute(get_relationship_action, family_tree_obj, ['Chit', 'Mother'])
        self.assertEqual(len(result['members_list']), 1)
        self.assertEqual(result['members_list'][0], first_member)

    def test_action_failure(self):
        invalid_action_type = 'ADD_TEST'
        result = member_action.execute(invalid_action_type, family_tree_obj, ['Anga', 'Shin', 'Male'])
        self.assertEqual(result['error_msg'], output_messages['INVALID_ACTION'])

