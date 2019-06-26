# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create_project(self, project):
        wd = self.app.wd
        self.open_create_page()
        self.select_to_add()
        self.fill_group_form(project)
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def fill_group_form(self, project):
        self.change_field_value('name', project.name)
        self.change_field_value('description', project.description)
        self.change_list('status', project.status)
        self.change_list("view_state", project.view_status)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_list(self, field_name, field_text):
        wd = self.app.wd
        if field_text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_value(field_text)
            #wd.find_element_by_name(field_name).click()

    def open_create_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def select_to_add(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_create_page()
        self.select_project(id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()

    def select_project(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(@href, 'manage_proj_edit_page.php?project_id=%s')]" %id).click()

    def get_project_list(self, count):
        wd = self.app.wd
        self.open_create_page()
        self.project_catch = []
        row_number = 1
        for i in range(count):
            row = wd.find_element_by_css_selector("tr.row-%s" % (row_number))
            elements_td = row.find_elements_by_tag_name('td')
            name = elements_td[0].text
            description = elements_td[4].text
            self.project_catch.append(Project(name=name, description=description))
            if row_number == 1:
                row_number = 2
            else:
                row_number = 1
        return list(self.project_catch)
