from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?WSDL#op.idm143337760")
        client.sd[0].service.setlocation("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php?WSDL")
        client.sd[0].service.setlocation("http://localhost/mantisbt-1.2.20/api/soap/mantisconnect.php")
        answer = []
        list = client.service.mc_projects_get_user_accessible(username, password)
        for row in list:
            answer.append(Project(id=str(row.id),
                                  name=row.name,
                                  status=row.status.id,
                                  view_status=row.view_state.id,
                                  description=row.description))
        return answer