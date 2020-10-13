from ..service import member


def add_relationship(input_data, relationship, family_tree):
    result = member.add_relationship(
        input_data,
        relationship,
        family_tree
    )
    return result
