import unittest
from src.constants import relationship_type, output_messages, member_gender
from src.service import member
from tests.helper import member as member_helper


class TestMember(unittest.TestCase):
    def test_add_child(self):
        relationship = relationship_type['CHILD']
        relationship_data = ['King Shan', 'Chit', 'Male']
        parent = member_helper.create_test_member('King Shan', member_gender['Male'])
        result = member.add_relationship(relationship_data, relationship)
        self.assertEqual(result, output_messages['CHILD_ADDITION_SUCCEEDED'])
