from model.project import Project

def test_del_project(app):
    app.session.login('administrator', 'root')
    app.project.delete_project_by_id(2)
