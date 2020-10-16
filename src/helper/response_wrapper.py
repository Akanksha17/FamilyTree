def get_member_name(member):
    return member.name


def get_member_name_string(members):
    names = list(map(get_member_name, members))
    return ' '.join(names)


def is_members_list_empty(members):
    if len(members) == 0:
        return True
    else:
        return False


def response_wrapper(result):
    if 'error_msg' in result.keys():
        return result['error_msg']

    if 'members_list' in result.keys():
        if not is_members_list_empty(result['members_list']):
            return get_member_name_string(result['members_list'])
        else:
            return 'None'
    else:
        return result.get('success_msg', 'SUCCESS')
