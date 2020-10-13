from src.models import member, family_tree
from src.constants import member_gender
from src.service import family_tree as family_tree_service
import logging


def initialise_family_tree():
    head_member = member.Member('King Shan', member_gender['Male'])
    family_tree_obj = family_tree.FamilyTree([head_member])
    logging.debug('Initialised family tree')

    family_tree_obj.set_head_member(head_member)
    test_data_file = open("set_up_commands.txt", "r")
    data_file_lines = test_data_file.readlines()

    logging.debug('Starting File handling for set up commands')
    for lines in data_file_lines:
        updated_family_tree, msg = family_tree_service.update_family_tree(
            family_tree_obj,
            lines
        )

        family_tree_obj = updated_family_tree

    test_data_file.close()
    logging.debug('Finished File handling for set up commands')
    return family_tree_obj


