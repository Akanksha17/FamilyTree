
from src.constants import output_messages, valid_actions, relationship_type as relationship_type_constants
from src.controller import member as member_controller
from src.validation import is_action_valid


def execute_add_action(action, family_tree_instance, arguments):
    action_map = {
        valid_actions['ADD_CHILD']: [member_controller.add_relationship, relationship_type_constants['CHILD']],
        valid_actions['ADD_SPOUSE']: [member_controller.add_relationship, relationship_type_constants['SPOUSE']]
    }
    action_func, rel_type = action_map[action][0], action_map[action][1]
    action_result = action_func(arguments, rel_type, family_tree_instance)
    return action_result


def execute(action, family_tree_instance, arguments):
    if not is_action_valid(action):
        return {
            'error_msg': output_messages.get('INVALID_ACTION', 'INVALID ACTION'),
            'updated_family_tree': family_tree_instance
        }

    if action == valid_actions['GET_RELATIONSHIP']:
        result = member_controller.get_relationship(arguments, family_tree_instance)
        return result
    else:
        return execute_add_action(action, family_tree_instance, arguments)