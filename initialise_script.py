from src.models import member, family_tree
from src.constants import member_gender
from src.service import family_tree as family_tree_service
import logging


def initialise_family_tree():
    new_member = member.Member('Anga', member_gender['FEMALE'])
    members = {
        'Anga': new_member
    }
    family_tree_obj = family_tree.FamilyTree(members)
    logging.debug('Initialised family tree')

    family_tree_obj.set_head_member(new_member)
    test_data_file = open("initial_input_commands.txt", "r")
    data_file_lines = test_data_file.readlines()

    logging.debug('Starting File handling for set up commands')
    for line in data_file_lines:
        updated_info = family_tree_service.update_family_tree(
            family_tree_obj,
            line.rstrip()
        )

        family_tree_obj = updated_info['updated_family_tree']

    test_data_file.close()
    logging.debug('Finished File handling for set up commands')
    return family_tree_obj


