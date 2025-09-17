from conftest import driver
from pages.login_page import LoginPage
from pages.records_page import RecordsPage
from pages.projects_page import ProjectsPage


def test_project_creation(driver):
    login_page = LoginPage(driver)
    records_page = RecordsPage(driver)
    projects_page = ProjectsPage(driver)

    login_page.login()
    records_page.records_click()
    records_page.projects_click()
    records_page.select_account_click()
    records_page.account_name_click()

    # Создание проекта
    records_page.add_click()
    projects_page.subject_project_input()
    projects_page.program_project_input()
    projects_page.program_project_click()
    projects_page.service_project_input()
    projects_page.service_project_click()
    projects_page.customer_project_input()
    projects_page.customer_project_click()
    projects_page.select_justification()
    projects_page.complete_save_operation()

    assert projects_page.get_status_project_text() == 'Зарегистрировано'