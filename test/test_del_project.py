from model.project import Project
import random

def test_del_project(app, db):
    app.session.login('administrator', 'root')
    if len(db.get_project_list()) == 0:
        app.project.create_project(Project(name='test', description='test'))
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project.id)
    new_projects = db.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(project)
    assert old_projects == new_projects