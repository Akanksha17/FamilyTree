from src.constants import output_messages, valid_actions, relationship_type
from src.controller import member as member_controller
from src.validation import is_action_valid


def execute(action, family_tree_instance, arguments=None):
    if not is_action_valid(action):
        return {
            'msg': output_messages.get('INVALID_ACTION', 'INVALID ACTION'),
            'updated_family_tree': family_tree_instance
        }
    action_map = {
        valid_actions['ADD_CHILD']: member_controller.add_relationship(
            arguments,
            relationship_type['CHILD'],
            family_tree_instance
        ),

        valid_actions['GET_RELATIONSHIP']: member_controller.get_relationship(
            arguments,
            family_tree_instance
        )
    }
    result = action_map.get(action)
    return result
