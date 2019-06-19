__author__ = 'Alex'

def test_add_project(app):
    app.session.login('administrator', 'root')
    app.project.create_project()