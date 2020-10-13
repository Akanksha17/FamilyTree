from ..validation import is_relationship_data_valid
from ..constants import output_messages
from ..models import member
from . import family_tree as family_tree_service


def add_parent(from_member, to_member):
    from_member.set_parent(to_member)


def add_spouse(from_member, to_member):
    from_member.set_spouse(to_member)


def add_child(from_member, to_member_name, gender, family_tree):
    to_member = member.Member(to_member_name, gender)
    from_member.set_child(to_member)
    msg = output_messages['CHILD_ADDITION_SUCCEEDED']
    updated_family_tree = family_tree_service.add_member(to_member, family_tree)

    return {
        'updated_family_tree': updated_family_tree,
        'msg': msg
    }


def add_relationship(relationship_data, relationship_type, family_tree):
    if not is_relationship_data_valid(relationship_type, relationship_data):
        return False

    from_member_name = relationship_data[1]
    to_member_name = relationship_data[2]
    from_member = family_tree['members'][from_member_name]
    gender = 'MALE'
    relationship_setter = {
        relationship_type['PARENT']: add_parent(from_member, to_member_name),
        relationship_type['SPOUSE']: add_spouse(from_member, to_member_name),
        relationship_type['CHILD']: add_child(from_member, to_member_name, gender)
    }
    return relationship_setter.get(relationship_type, 'Invalid')
