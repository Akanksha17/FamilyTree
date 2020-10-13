from .src.validation import is_empty_user_input
from .src.router.family_tree import execute_action


def start_family_tree(user_input):
    if is_empty_user_input(input_from_user):
        error_msg = 'Invalid Input'
        return error_msg

    input_list = user_input.split(' ')
    action = input_list[0]
    message = execute_action(action, input_list[1::])
    return message


if __name__ == '__main__':
    input_from_user = input('Enter command: ')
    result = start_family_tree(input_from_user)
    print(result)
