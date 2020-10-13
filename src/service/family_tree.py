from src.validation import is_empty_user_input
from src.router.family_tree import execute_action


def add_member(member, family_tree):
    family_tree['members'][member.name] = member
    return family_tree


def update_family_tree(family_tree_instance, input_command):
    if is_empty_user_input(input_command):
        error_msg = 'Invalid Input Command'
        return error_msg
    print()
    input_list = input_command.split(' ')
    action = input_list[0]
    execution_result = execute_action(action, family_tree_instance,  input_list[1::])
    return execution_result
