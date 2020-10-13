

def add_parent(from_member, to_member):
    from_member.set_parent(to_member)


def add_spouse(from_member, to_member):
    from_member.set_spouse(to_member)


def add_child(from_member, to_member):
    from_member.set_child(to_member)


def add_relationship(from_member, to_member, relationship_type):
    relationship_setter = {
        relationship_type['PARENT']: add_parent(from_member, to_member),
        relationship_type['SPOUSE']: add_spouse(from_member, to_member),
        relationship_type['CHILD']: add_child(from_member, to_member)
    }
    return relationship_setter.get(relationship_type, 'Invalid')
