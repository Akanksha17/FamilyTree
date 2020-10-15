from src.models import member


def create_test_member(name, gender):
    return member.Member(name, gender)


def create_test_members(member_list):
    new_members = []
    for member_obj in member_list:
        new_member = create_test_member(member_obj['name'], member_obj['gender'])
        new_members.append(new_member)
    return new_members

