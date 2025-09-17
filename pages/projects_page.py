
from pages.common_methods import CommonMethods
from pages.locators import ProjectsPageLocators, CommonLocators

class ProjectsPage(CommonMethods):

    def projects_click(self):
        return self.click(ProjectsPageLocators.BUTTON_PROJECTS)

    def add_project_click(self):
        return self.click(CommonLocators.BUTTON_ADD)

    def subject_project_input(self, text="Тестовый"):
        return self.input_text(ProjectsPageLocators.INPUT_SUBJECT_PROJECT, text)

    def service_project_input(self, text="ПЗПП. ПП. Управление знаниями"):
        return self.input_text(ProjectsPageLocators.INPUT_SERVICE_PROJECT, text)

    def service_project_click(self):
        return self.click(ProjectsPageLocators.BUTTON_SELECT_SERVICE_PROJECT)

    def program_project_input(self, text="1"):
        return self.input_text(ProjectsPageLocators.INPUT_PROGRAM_PROJECT, text)

    def program_project_click(self):
        return self.click(ProjectsPageLocators.BUTTON_SELECT_PROGRAM_PROJECT)

    def customer_project_input(self, text="ДИТ. Госуслуги Москвы.Внешние подрядчики"):
        return self.input_text(ProjectsPageLocators.INPUT_CUSTOMER_PROJECT, text)

    def customer_project_click(self):
        return self.click(ProjectsPageLocators.BUTTON_SELECT_CUSTOMER_PROJECT)

    def select_justification(self):
        return self.select_by_visible_text(
            ProjectsPageLocators.DROPDOWN_JUSTIFICATION_PROJECT,
            "Соответствие"
        )

    def get_status_project_text(self):
        status_element = self.find_element(ProjectsPageLocators.PROJECT_STATUS)
        return status_element.text.strip()

    def complete_project_save(self):
        """Специфичный метод сохранения для проектов"""
        return self.complete_save_operation()