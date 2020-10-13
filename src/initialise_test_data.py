from .test_data import members_to_add, relationships_to_add
from .models import member, relationship
from .constants import relationship_def_backtrace, relationship_type


def initialise_members(members=None, head_member=None):
    if members is None:
        members = {}
    for i in members_to_add:
        members[i['name']] = member.Member(i)
        if head_member is None:
            head_member = members[i['name']]
    return members, head_member


def add_parent(from_member, to_member):
    from_member.set_parent(to_member)


def add_spouse(from_member, to_member):
    from_member.set_spouse(to_member)


def add_child(from_member, to_member):
    from_member.set_child(to_member)


def add_relationship(from_member, to_member, relationship_type):
    relationship_setter = {
        relationship_type['PARENT']: add_parent(from_member, to_member),
        relationship_type['SPOUSE']: add_spouse(from_member, to_member),
        relationship_type['CHILD']: add_child(from_member, to_member)
    }
    return relationship_setter.get(relationship_type, 'Invalid')


def initialise_relationships(relationships, members):
    for j in relationships:
        from_member = members[j['from']]
        to_member = members[j['to']]
        relationship_obj = relationship.Relationship(to_member, j['relationship'])
        from_member.add_relationship(relationship_obj)


def initialise_family_tree():
    family_members, head_member = initialise_members()
    initialise_relationships(relationships_to_add, family_members)
    return head_member


head_member = initialise_family_tree()


def get_relationship(member_name, relationship):
    relationship_def = relationship_def_backtrace[relationship]
    visited_members = []
    member_stack = [head_member]
    while len(member_stack) != 0:
        current_member = member_stack[0]
        if current_member.name in visited_members:
            break
        else:
            visited_members.append(current_member.name)
            member_stack.pop()
            member.get_relationship()
            member_stack.append()


