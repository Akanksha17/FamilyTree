import unittest
from src.controller import member as member_controller
from src.constants import valid_actions, member_gender, relationship_type, output_messages
from src.models import member as member_model, family_tree as family_tree_model

child_relationship = relationship_type['CHILD']
get_relationship_action = valid_actions['GET_RELATIONSHIP']

first_member = member_model.Member('Anga', member_gender['FEMALE'])
members_obj = {
    'Anga': first_member
}

family_tree_obj = family_tree_model.FamilyTree(members_obj)
family_tree_obj.set_head_member(first_member)


class TestMemberController(unittest.TestCase):
    def test_add_relationship_success(self):
        result = member_controller.add_relationship(['Anga', 'Chit', 'Male'],
                                                    child_relationship,
                                                    family_tree_obj)
        self.assertEqual(result['msg'], output_messages['CHILD_ADDITION_SUCCEEDED'])
        newly_added_member = result['updated_family_tree'].members['Chit']
        parent = newly_added_member.get_parent()
        self.assertEqual(parent, first_member)

    def test_add_relationship_failure(self):
        result = member_controller.add_relationship(['Anga', 'Chit', 'Male'],
                                                    'Test',
                                                    family_tree_obj)

        self.assertEqual(result['msg'], output_messages['CHILD_ADDITION_FAILED'])

    def test_get_relationship_success(self):
        added_result = member_controller.add_relationship(['Anga', 'Chit', 'Male'],
                                                          child_relationship,
                                                          family_tree_obj)
        result = member_controller.get_relationship(['Shan', 'Son'], added_result['updated_family_tree'])
        self.assertEqual(len(result['members_list']), 1)
        self.assertEqual(result['members_list'][0].name, 'Chit')

    def test_get_relationship_none_case(self):
        result = member_controller.get_relationship(['Shan', 'Daughter'], family_tree_obj)
        self.assertEqual(len(result['members_list']), 0)
