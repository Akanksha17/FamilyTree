from initialise_script import initialise_family_tree
import os


if __name__ == '__main__':
    print('Welcome to the Family of King Shan')
    user_file_input = input('Enter path of your test file: ')
    assert os.path.exists(user_file_input), "I did not find the file at, " + str(user_file_input)
    family_tree = initialise_family_tree()
    # print(family_tree.get_head_member(), 'head member')
    # result = update_family_tree(family_tree, input_from_user)
    # print(result['msg'])
