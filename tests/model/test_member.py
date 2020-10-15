import unittest
from src.models import member
from src.constants import member_gender
from tests.helper import member as member_helper


class TestMember(unittest.TestCase):
    def test_member_init(self):
        new_member = member.Member('King Shan', member_gender['M'])
        self.assertEqual(new_member.gender, member_gender['MALE'])
        self.assertEqual(new_member.name, 'King Shan')

    def test_member_parent(self):
        member_details = [
            {
                'name': 'Chit',
                'gender': member_gender['MALE']
            },
            {
                'name': 'King Shan',
                'gender': member_gender['MALE']
            },
        ]
        members = member_helper.create_test_members(member_details)
        member1 = members[0]
        member2 = members[1]

        member1.set_parent(member2)
        updated_member_parent = member1.get_parent()
        self.assertEqual(updated_member_parent.name, 'King Shan')
        self.assertEqual(updated_member_parent.gender,  member_gender['MALE'])

    def test_member_spouse(self):
        member_details = [
            {
                'name': 'King Shan',
                'gender': member_gender['MALE']
            },
            {
                'name': 'Queen Anga',
                'gender': member_gender['FEMALE']
            },
        ]

        members = member_helper.create_test_members(member_details)
        member1 = members[0]
        member2 = members[1]

        member1.set_spouse(member2)
        updated_member_spouse = member1.get_spouse()
        self.assertEqual(updated_member_spouse.name, 'Queen Anga')
        self.assertEqual(updated_member_spouse.gender,  member_gender['FEMALE'])

    def test_member_child(self):
        member_details = [
            {
                'name': 'King Shan',
                'gender': member_gender['MALE']
            },
            {
                'name': 'Chit',
                'gender': member_gender['MALE']
            },
        ]

        members = member_helper.create_test_members(member_details)
        member1 = members[0]
        member2 = members[1]

        member1.set_children(member2)
        member_children = member1.get_children()
        self.assert_('Chit' in member_children.keys())
        self.assertEqual(member_children['Chit'].name, 'Chit')
        self.assertEqual(member_children['Chit'].gender,  member_gender['MALE'])


if __name__ == '__main__':
    unittest.main()
