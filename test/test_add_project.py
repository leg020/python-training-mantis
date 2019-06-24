__author__ = 'Alex'
from model.project import Project
from data.project import testdata

def test_add_project(app, data_project, db):
    project = data_project
    app.session.login('administrator', 'root')
    old_project = db.get_project_list()
    app.project.create_project(project)
    app.soap.get_project('administrator', "root")
    new_project = db.get_project_list()
    assert len(old_project) + 1 == len(new_project)
    old_project.append(project)
    assert sorted(old_project, key=Project.id_or_max) == sorted(new_project, key=Project.id_or_max)
