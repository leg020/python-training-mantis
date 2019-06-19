# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create_project(self):
        wd = self.app.wd
        self.open_create_page()
        self.fill_group_form()
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def fill_group_form(self):
        self.change_field_value('name', 'project4')
        self.change_field_value('description', 'description4')
        self.change_list('status', 'release')
        self.change_list("view_state", 'public')

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
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(field_text)
            wd.find_element_by_name(field_name).click()

    def open_create_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()


