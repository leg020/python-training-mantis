__author__ = "Alex"

class Project:
    def __init__(self, name=None, description=None,
                 status=None, view_status=None):
        self.name = name
        self.description = description
        self.status = status
        self.view_status = view_status