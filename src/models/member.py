
class Member:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.gender = kwargs['gender']
        self._spouse = None
        self._child = None
        self._parent = None

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self):
        return self._parent

    def set_spouse(self, spouse):
        self._parent = spouse

    def get_spouse(self):
        return self._spouse

    def set_child(self, child):
        self._child = child

    def get_child(self):
        return self._child
