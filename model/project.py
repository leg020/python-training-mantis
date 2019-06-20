__author__ = "Alex"
from sys import maxsize

class Project:
    def __init__(self, name=None, description=None,
                 status=None, view_status=None, id=None):
        self.name = name
        self.description = description
        self.status = status
        self.view_status = view_status
        self.id = id

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize