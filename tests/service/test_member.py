import unittest
from src.constants import relationship_type, output_messages, member_gender
from src.service import member as member_service
from tests.data_helper import member as test_member_helper, family_tree as test_family_tree_helper

child_relationship = relationship_type['CHILD']
add_child_relationship_data = ['Shan', 'Chit', 'MALE']
parent = test_member_helper.create_test_member('Shan', member_gender['MALE'])
family_tree = test_family_tree_helper.create_family_tree({'Shan': parent}, parent)


class TestMember(unittest.TestCase):
    def test_add_child_success(self):
        result = member_service.add_relationship(add_child_relationship_data, child_relationship, family_tree)
        self.assertEqual(result['msg'], output_messages['CHILD_ADDITION_SUCCEEDED'])

        updated_family_tree = result['updated_family_tree']
        newly_created_child = updated_family_tree.members['Chit']
        self.assertEqual(newly_created_child.get_parent(), parent)

    def test_get_parent_success(self):
        result = member_service.add_relationship(add_child_relationship_data, child_relationship, family_tree)
        updated_family_tree = result['updated_family_tree']
        newly_created_child = updated_family_tree.members['Chit']
        self.assertEqual(newly_created_child.get_parent(), parent)

    def test_get_relationship_success(self):

        result = member_service.add_relationship(add_child_relationship_data, child_relationship, family_tree)
        updated_family_tree = result['updated_family_tree']
        result = member_service.get_relationship(['Chit', 'Father'], updated_family_tree)
        self.assertEqual(result['members_list'][0], parent)

    def test_add_child_failure(self):
        mock_relationship_data = ['Kriya', 'Chit', 'FEMALE']
        result = member_service.add_relationship(mock_relationship_data, child_relationship, family_tree)
        self.assertEqual(result['msg'], output_messages['PERSON_NOT_FOUND'])


if __name__ == '__main__':
    unittest.main()
