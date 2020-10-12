# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from .src.models import member
from .src.constants import member_gender, relationship_unit


def print_hi(name):
    king = member.Member('King Shan', member_gender['MALE'])
    members_to_add = [
        {
            'name': 'King Shan',
            'gender': member_gender['MALE']
        },
        {
            'name': 'Queen Anga',
            'gender': member_gender['FEMALE']
        },
        
    ]
    member_relationships_to_add = [{
        'to': king,
        'from': member.Member('Queen Anga', member_gender['FEMALE']),
        'relationship': relationship_unit['FEMALE_SPOUSE']
    },
        {

        }
    ]
    relationship = relationship_unit['FEMALE_SPOUSE']
    king.add_relationship(relationship)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
