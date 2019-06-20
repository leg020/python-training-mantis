__author__ = 'Alex'
from model.project import Project
from data.project import testdata

def test_add_project(app, json_project, db):
    project = json_project
    app.session.login('administrator', 'root')
    app.project.create_project(project)
    print(db.get_project_list())