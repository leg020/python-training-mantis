from suds.client import Client
from suds import WebFault

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False