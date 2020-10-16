from initialise_script import initialise_family_tree
import os
import sys
from src.helper import file_handler
from src.helper.response_wrapper import response_wrapper
import logging

if __name__ == '__main__':
    user_file_input = sys.argv[1]
    assert os.path.exists(user_file_input), "did not find the file at, " + str(user_file_input)
    family_tree = initialise_family_tree()
    logging.debug('Initialised Family Tree')
    file_handler.execute_file_input(user_file_input, family_tree)
