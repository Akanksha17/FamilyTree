from .constants import valid_actions, relationship_type


def is_empty_user_input(user_input):
    if user_input is None:
        return True
    else:
        return False


def is_action_valid(action):
    if action in valid_actions.values():
        return True
    else:
        return False


def is_relationship_data_valid(relationship, input_data):
    relationship_args_map = {
        relationship_type['CHILD']: 3,
        relationship_type['SPOUSE']: 2
    }
    if len(input_data) < relationship_args_map[relationship]:
        return False
    else:
        return True


def validate_relationship_data(relationship, input_data):
    if not is_relationship_data_valid(relationship, input_data):
        return False
    else:
        return True

