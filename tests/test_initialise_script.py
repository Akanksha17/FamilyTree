import unittest
from src.constants import member_gender
from initialise_script import initialise_family_tree


def update_family_tree(family_tree_instance, input_command):
    if is_empty_user_input(input_command):
        error_msg = 'Invalid Input Command'
        return error_msg

    input_list = input_command.split(' ')
    action = input_list[0]
    logging.info('Action requested:', action)
    print('action', action)
    execution_result = execute_action(action, family_tree_instance,  input_list[1::])
    return execution_result

class TestInitialiseScript(unittest.TestCase):
    def test_initialise_script_success(self):
        family_tree = initialise_family_tree()
        head_member = family_tree.get_head_member()
        self.assertEqual(head_member.name, 'Shan')
        self.assertEqual(head_member.gender, member_gender['Male'])


if __name__ == '__main__':
    unittest.main()

