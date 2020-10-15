from src.constants import valid_actions, relationship_type, member_gender, output_messages
from src.relationship_definition import relationship_def


def is_empty_user_input(user_input):
    if user_input is None or user_input == '':
        return True
    else:
        return False


def is_action_valid(action):
    if action in valid_actions.values():
        return True
    else:
        return False


def is_relationship_args_valid(relationship, input_data):
    relationship_args_map = {
        relationship_type['CHILD']: 3,
        relationship_type['SPOUSE']: 3
    }
    if len(input_data) < relationship_args_map[relationship]:
        return False
    else:
        return True


def is_relationship_type_valid(relationship):
    if relationship.upper() in relationship_type.keys():
        return True
    else:
        return False


def is_gender_valid(gender):
    if gender.upper() in member_gender.keys():
        return True
    return False


def is_relationship_data_valid(relationship_name, input_data):
    if not is_relationship_type_valid(relationship_name)\
            or not is_relationship_args_valid(relationship_name, input_data):
        return False, {'error_message': output_messages['CHILD_ADDITION_FAILED']}

    gender = input_data[2]
    if not is_gender_valid(gender):
        return False, {'error_message': output_messages['CHILD_ADDITION_FAILED']}

    return True, {'error_message': None}


def is_relationship_query_valid(relationship):
    if relationship.upper() in relationship_def.keys():
        return True
    return False

