from initialise_script import initialise_family_tree
import os
from src.action.family_tree import execute_file_input

if __name__ == '__main__':
    print('Welcome to the Family of King Shan')
    user_file_input = input('Enter path of your test file: ')
    assert os.path.exists(user_file_input), "I did not find the file at, " + str(user_file_input)
    family_tree = initialise_family_tree()
    execute_file_input(user_file_input, family_tree)
