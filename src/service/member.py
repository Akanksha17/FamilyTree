from src.validation import is_relationship_data_valid, is_relationship_query_valid
from src.constants import output_messages, relationship_type as relationship_type_constants, \
    relationship_def, member_gender
from src.models import member
from src.service import family_tree as family_tree_service
import copy


def add_parent(from_member, to_member, family_tree):
    from_member.set_parent(to_member)


def add_spouse(from_member, to_member, family_tree):
    from_member.set_spouse(to_member)


def add_child(from_member, to_member_name, gender, family_tree):
    to_member = member.Member(to_member_name, gender)
    from_member.set_children(to_member)
    to_member.set_parent(from_member)
    msg = output_messages['CHILD_ADDITION_SUCCEEDED']
    updated_family_tree = family_tree_service.add_member(to_member, family_tree)

    return {
        'updated_family_tree': updated_family_tree,
        'msg': msg
    }


def add_relationship(relationship_data,
                     relationship_type,
                     family_tree_instance
                     ):
    if not is_relationship_data_valid(relationship_type, relationship_data):
        return False

    from_member_name = relationship_data[0]
    to_member_name = relationship_data[1]
    gender = relationship_data[2].upper()
    from_member = family_tree_instance.members.get(from_member_name)
    if from_member:
        print('--------***********', from_member)
        relationship_setter = {
            relationship_type_constants['PARENT']: add_parent(from_member,
                                                              to_member_name,
                                                              family_tree_instance),

            relationship_type_constants['SPOUSE']: add_spouse(from_member,
                                                              to_member_name,
                                                              family_tree_instance),

            relationship_type_constants['CHILD']: add_child(from_member,
                                                            to_member_name,
                                                            gender,
                                                            family_tree_instance)
        }
        return relationship_setter.get(relationship_type, 'Invalid')
    else:
        return {
            'msg': output_messages['PERSON_NOT_FOUND'],
            'updated_family_tree': family_tree_instance
        }


def get_parent(member_obj, parent_gender):
    member_parent = member_obj.get_parent()
    if member_gender['N/A'] == parent_gender\
            or member_parent.gender == parent_gender:
        return [member_parent]
    else:
        return [member_parent.get_spouse()]


def get_spouse(member_obj):
    return member_obj.get_spouse()


def get_child(member_obj, child_gender):
    member_children = member_obj.get_children()
    if child_gender.upper() == member_gender['N/A']:
        return member_children
    else:
        return list(
            filter(lambda child: child['gender'] == child_gender.upper(), member_children))


def relationship_switch(to_member, relationship_unit):
    relationship_def_switch = {
        relationship_type_constants['PARENT']: get_parent(to_member,
                                                          relationship_unit.get('gender')),

        relationship_type_constants['SPOUSE']: get_spouse(to_member),

        relationship_type_constants['CHILD']: get_child(to_member,
                                                        relationship_unit.get('gender'))
    }
    return relationship_def_switch.get(relationship_unit.get('type'), 'Invalid')


def find_member_relationship(relationship_trace_def, to_member):
    current_member = copy.deepcopy(to_member)
    result_members = [current_member]
    for unit in relationship_trace_def:
        result_members = relationship_switch(to_member, unit)
    return result_members


def get_relationship(arguments, family_tree_instance):
    to_member_name = arguments[0]
    relationship_name = arguments[1]
    if not is_relationship_query_valid(relationship_name):
        return False
    to_member = family_tree_instance.members[to_member_name]
    relationship_trace = relationship_def[relationship_name.upper()]
    final_result = []
    result = [to_member]
    for rel in relationship_trace:
        for member_value in result:
            if len(result) == 0:
                break
            result = find_member_relationship(rel, member_value)
            final_result.extend(result)
        return final_result




    pass
