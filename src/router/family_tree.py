from ..constants import output_messages, valid_actions, relationship_type
from ..controller import member as member_controller


def execute_action(action, arguments=None):
    action_map = {
        valid_actions['ADD_CHILD']: member_controller.add_relationship(
            arguments,
            relationship_type['CHILD']
        ),

        valid_actions['GET_RELATIONSHIP']: member_controller.get_relationship(
            arguments
        )
    }
    invalid_action_msg = output_messages.get('INVALID_ACTION', 'INVALID ACTION')
    return action_map.get(action, invalid_action_msg)
