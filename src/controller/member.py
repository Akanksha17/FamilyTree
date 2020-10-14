from src.service import member as member_service


def add_relationship(arguments, relationship, family_tree_instance):
    result = member_service.add_relationship(
        arguments,
        relationship,
        family_tree_instance
    )
    return result


def get_relationship(arguments, family_tree_instance):
    result = member_service.get_relationship(
        arguments,
        family_tree_instance
    )
    return result
