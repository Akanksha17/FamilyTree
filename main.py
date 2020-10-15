from initialise_script import initialise_family_tree
import os
import sys
from src.action.file import execute_file_input

if __name__ == '__main__':
    user_file_input = sys.argv[1]
    assert os.path.exists(user_file_input), "I did not find the file at, " + str(user_file_input)
    family_tree = initialise_family_tree()
    execute_file_input(user_file_input, family_tree)
