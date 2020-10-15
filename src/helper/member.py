from src.constants import member_gender as member_gender_constant,\
    output_messages, relationship_type as relationship_type_constant
from src.relationship_definition import direct_relationship
from src.service import family_tree as family_tree_service
from src.models import member as member_model


def get_father(member_obj):
    father = member_obj.get_parent(member_gender_constant['MALE'])
    if father:
        return [father]
    else:
        return []


def get_mother(member_obj):
    mother = member_obj.get_parent(member_gender_constant['FEMALE'])
    if mother:
        return [mother]
    else:
        return []


def get_sister(member_obj):
    sister = member_obj.get_sibling(member_gender_constant['FEMALE'])
    if sister:
        return sister
    else:
        return []


def get_brother(member_obj):
    brother = member_obj.get_sibling(member_gender_constant['MALE'])
    if brother:
        return brother
    else:
        return []


def get_parent(member_obj):
    member_parent = member_obj.get_parent()
    if member_parent:
        return [member_parent]
    else:
        []


def get_spouse(member_obj):
    member_spouse = member_obj.get_spouse()
    if member_spouse:
        return [member_spouse]
    return []


def get_child(member_obj):
    member_children = member_obj.get_children()
    if member_children:
        return member_children.values()
    else:
        return []


def direct_relationship_switch(to_member, relationship):
    switch = {
        direct_relationship['FATHER']: get_father,
        direct_relationship['MOTHER']: get_mother,
        direct_relationship['BROTHER']: get_brother,
        direct_relationship['SISTER']: get_sister,
    }
    func = switch[relationship]
    return func(to_member)


def add_spouse(from_member, to_member_name, gender, family_tree):
    to_member = member_model.Member(to_member_name, gender)
    from_member.set_spouse(to_member)
    updated_family_tree = family_tree_service.add_member(to_member, family_tree)
    msg = output_messages['SPOUSE_ADDITION_SUCCEEDED']
    return {
        'updated_family_tree': updated_family_tree,
        'msg': msg
    }


def add_child(from_member, to_member_name, gender, family_tree):
    to_member = member_model.Member(to_member_name, gender)
    from_member.set_children(to_member)
    to_member.set_parent(from_member)
    updated_family_tree = family_tree_service.add_member(to_member, family_tree)
    msg = output_messages['CHILD_ADDITION_SUCCEEDED']
    return {
        'updated_family_tree': updated_family_tree,
        'msg': msg
    }


def add_relationship_switch(from_member, to_member_name, family_tree_instance, relationship_type, gender):
    relationship_switcher = {
        relationship_type_constant['SPOUSE']: add_spouse,

        relationship_type_constant['CHILD']: add_child
    }
    rel_func = relationship_switcher[relationship_type]
    return rel_func(from_member, to_member_name, gender, family_tree_instance)

