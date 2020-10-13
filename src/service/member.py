from ..validation import is_relationship_data_valid
from ..constants import output_messages
from ..models import member


def add_parent(from_member, to_member):
    from_member.set_parent(to_member)


def add_spouse(from_member, to_member):
    from_member.set_spouse(to_member)


def add_child(from_member, to_member, gender):
    new_member = member.Member(to_member, gender)
    from_member.set_child(new_member)
    msg = output_messages['CHILD_ADDITION_SUCCEEDED']
    return msg


def add_relationship(input_data, relationship_type):
    if not is_relationship_data_valid(relationship_type, input_data):
        return False

    from_member = input_data[1]
    to_member = input_data[2]
    gender = input_data[3]
    relationship_setter = {
        relationship_type['PARENT']: add_parent(from_member, to_member),
        relationship_type['SPOUSE']: add_spouse(from_member, to_member),
        relationship_type['CHILD']: add_child(from_member, to_member, gender)
    }
    return relationship_setter.get(relationship_type, 'Invalid')
