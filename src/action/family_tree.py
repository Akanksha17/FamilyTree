from src.service import family_tree as family_tree_service


def execute_file_input(file_path, family_tree_instance):
    input_data_file = open(file_path, "r")
    data_file_lines = input_data_file.readlines()
    for line in data_file_lines:
        updated_info = family_tree_service.update_family_tree(
            family_tree_instance,
            line.rstrip()
        )
        print(updated_info['msg'])

        family_tree_instance = updated_info['updated_family_tree']
    return family_tree_instance
