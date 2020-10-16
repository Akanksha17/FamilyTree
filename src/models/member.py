from src.constants import member_gender
import copy

class Member:
    def __init__(self, name, gender, **kwargs):
        self.name = name
        self.gender = gender
        self._spouse = None
        self._children = {}
        self._parent = None

    def set_parent(self, parent):
        self._parent = parent

    def get_parent(self, gender=None):
        parent = self._parent
        if not gender or (gender and gender == parent.gender):
            return parent
        else:
            return parent.get_spouse()

    def set_spouse(self, spouse):
        self._spouse = spouse

    def get_spouse(self):
        return self._spouse

    def set_children(self, child):
        name = child.name
        self._children[name] = child

    def get_children(self, gender=None):
        children = self._children
        if not gender:
            return children
        else:
            children_list = []
            for key, value in children.items():
                if value.gender == gender:
                    children_list.append(value)

    def get_sibling(self, gender=None):
        parent = self.get_parent()
        parent_children = {}
        if parent:
            parent_children = parent.get_children()

        parent_children_cp = copy.deepcopy(parent_children)

        current_member_name = self.name
        if current_member_name in parent_children_cp.keys():
            parent_children_cp.pop(current_member_name)
        if not gender:
            return parent_children_cp.values()
        else:
            sibling_list = []
            for key, value in parent_children_cp.items():
                if value.gender == gender:
                    sibling_list.append(value)
            return sibling_list
