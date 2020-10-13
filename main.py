# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from .src.models import member
from .src.constants import member_gender, relationship_unit


def isEmptyUserInput(user_input):
    if user_input is None:
        return True
    else:
        return False


def start_family_tree(user_input):
    if isEmptyUserInput(input_from_user):
        error_msg = 'Invalid Input'
        return error_msg

    input_list = user_input.split(' ')
    action = input_list[0]
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_from_user = input('Enter command: ')
    start_family_tree(input_from_user)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
