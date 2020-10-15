from src.validation import is_empty_user_input
from src.action import member as member_action
from src.constants import output_messages
import logging


def add_member(member, family_tree):
    family_tree.members[member.name] = member
    return family_tree


def update_family_tree(family_tree_instance, input_command):
    if is_empty_user_input(input_command):
        error_msg = output_messages['INVALID_INPUT']
        return {'msg': error_msg, 'updated_family_tree': family_tree_instance}

    input_list = input_command.split(' ')
    action = input_list[0]
    logging.debug('Action requested:', action)

    execution_result = member_action.execute(action, family_tree_instance,  input_list[1::])
    return execution_result
