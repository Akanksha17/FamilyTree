
from src.constants import output_messages
from src.validation import is_empty_user_input
from src.action import member as member_action
import re
from src.helper.response_wrapper import response_wrapper


def execute_file_input(file_path, family_tree_instance):
    input_data_file = open(file_path, "r")
    data_file_lines = input_data_file.readlines()
    for line in data_file_lines:
        if is_empty_user_input(line.strip()):
            error_msg = output_messages['INVALID_INPUT']
            return {'error_msg': error_msg}

        input_string = re.sub(' +', ' ', line.strip())
        input_command = input_string.split(' ')
        action = input_command[0]
        execution_result = member_action.execute(action, family_tree_instance, input_command[1::])
        improved_response = response_wrapper(execution_result)
        print(improved_response)
    return
