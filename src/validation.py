from .constants import valid_actions, relationship_type, relationship_def, member_gender, output_messages


def is_empty_user_input(user_input):
    if user_input is None:
        return True
    else:
        return False


def is_action_valid(action):
    print(action)
    if action in valid_actions.values():
        return True
    else:
        return False


def is_relationship_args_valid(relationship, input_data):
    relationship_args_map = {
        relationship_type['CHILD']: 3,
        relationship_type['SPOUSE']: 2
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
    if not is_relationship_type_valid(relationship_name):
        return False, {'error_message': output_messages['INVALID_RELATIONSHIP_TYPE']}

    if not is_relationship_args_valid(relationship_name, input_data):
        return False, {'error_message': output_messages['INVALID_NUMBER_OF_ARGS']}

    gender = input_data[2]

    if not is_gender_valid(gender):
        return False, {'error_message': output_messages['INVALID_GENDER']}

    return True, {'error_message': None}


def is_relationship_query_valid(relationship):
    if relationship.upper() in relationship_def.keys():
        return True
    return False

