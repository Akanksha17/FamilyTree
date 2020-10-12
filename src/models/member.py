
class Member:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.gender = kwargs['gender'],
        self._relationships = []

    def add_relationship(self, relationship):
        self._relationships.append(relationship)
