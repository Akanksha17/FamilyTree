from src.constants import output_messages, valid_actions, relationship_type
from src.controller import member as member_controller


def router(action, family_tree_instance, arguments=None):
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
    invalid_action_msg = output_messages.get('INVALID_ACTION', 'INVALID ACTION')
    result = action_map.get(action, invalid_action_msg)
    return result
