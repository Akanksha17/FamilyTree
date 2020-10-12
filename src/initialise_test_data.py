from .test_data import members_to_add, relationships_to_add
from .models import member, relationship


def initialise_family_tree():
    members = {}
    for i in members_to_add:
        members[i['name']] = member.Member(i)
    for j in relationships_to_add:
        from_member = members[j['from']]
        to_member = members[j['to']]
        relationship_obj = relationship.Relationship(to_member, j['relationship'])
        from_member.add_relationship(relationship_obj)
