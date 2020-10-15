from src.validation import is_relationship_data_valid, is_relationship_query_valid
from src.constants import output_messages, relationship_type as relationship_type_constants
from src.models import member as member_model
from src.service import family_tree as family_tree_service
from src.relationship_definition import indirect_relationship, direct_relationship
from src.helper import member as member_helper


def add_relationship(relationship_data,
                     relationship_type,
                     family_tree_instance
                     ):
    valid, msg_obj = is_relationship_data_valid(relationship_type, relationship_data)
    if not valid:
        return {
            'msg': msg_obj.get('error_message', output_messages['CHILD_ADDITION_FAILED']),
            'updated_family_tree': family_tree_instance
        }

    from_member_name = relationship_data[0]
    to_member_name = relationship_data[1]
    gender = relationship_data[2].upper()
    from_member = family_tree_instance.members.get(from_member_name)
    if from_member:
        return member_helper.add_relationship_switch(from_member, to_member_name, family_tree_instance, relationship_type, gender)
    else:
        return {
            'msg': output_messages['PERSON_NOT_FOUND'],
            'updated_family_tree': family_tree_instance
        }


def get_relationship(arguments, family_tree_instance):
    to_member_name = arguments[0]
    relationship_name = arguments[1]

    if not is_relationship_query_valid(relationship_name):
        return {
            'msg': output_messages['RELATIONSHIP_UNSUPPORTED'],
            'members_list': []
        }

    to_member = family_tree_instance.members[to_member_name]
    if relationship_name.upper() in direct_relationship.keys():
        direct_relationship_obj = direct_relationship[relationship_name.upper()]
        members_final_list = member_helper\
            .direct_relationship_switch(to_member, direct_relationship_obj)
    else:
        relationship_trace = indirect_relationship[relationship_name.upper()]
        final_result = []
        start_members = [to_member]
        result1 = []
        for rel in relationship_trace:
            for unit in rel:
                for member_obj in start_members:
                    result1 = member_helper.direct_relationship_switch(member_obj, unit)
                start_members = result1
            final_result.extend(result1)
        members_final_list = final_result
    return {'msg': output_messages['SUCCESS'], 'members_list': members_final_list}
