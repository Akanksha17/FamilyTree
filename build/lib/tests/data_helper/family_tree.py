from src.models import family_tree as family_tree_model


def create_family_tree(members, head_member):
    family_tree = family_tree_model.FamilyTree(members)
    family_tree.set_head_member(head_member)
    return family_tree
