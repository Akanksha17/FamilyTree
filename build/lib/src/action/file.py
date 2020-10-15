from src.constants import output_messages
from src.validation import is_empty_user_input
from src.action import member as member_action


def execute_file_input(file_path, family_tree_instance):
    input_data_file = open(file_path, "r")
    data_file_lines = input_data_file.readlines()
    for line in data_file_lines:
        if is_empty_user_input(line.rstrip()):
            error_msg = output_messages['INVALID_INPUT']
            print(error_msg)

        input_command = line.rstrip().split(' ')
        action = input_command[0]
        member_action.execute(action, family_tree_instance, input_command[1::])
