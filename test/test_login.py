__author__ = 'Alex'

def test_login(app):
    #app.open_home_page()
    app.session('administrator', 'root')
    assert app.session.is_logged_in_as('administrator')