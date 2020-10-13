class FamilyTree:
    def __init__(self, members):
        self.members = members
        self._head_member = None

    def set_head_member(self, head_member):
        self._head_member = head_member

    def get_head_member(self):
        return self._head_member

