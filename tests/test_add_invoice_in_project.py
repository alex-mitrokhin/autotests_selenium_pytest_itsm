from conftest import driver
from pages.login_page import LoginPage
from pages.records_page import RecordsPage
from pages.projects_page import ProjectsPage


def test_add_invoice_in_project(driver):
    login_page = LoginPage(driver)
    records_page = RecordsPage(driver)
    projects_page = ProjectsPage(driver)

    login_page.login()
    records_page.records_click()
    records_page.projects_click()
    records_page.select_account_click()
    records_page.account_name_click()

    projects_page.existing_project_click()
    projects_page.add_invoice_click()
    projects_page.supplier_invoice_input()
    projects_page.supplier_invoice_click()
    projects_page.number_invoice_input()
    projects_page.input_date_via_js()
    projects_page.unit_price_invoice_input()
    projects_page.quantity_invoice_input()
    projects_page.complete_save_operation()

    assert projects_page.get_amount_invoice_text() == '20,000.00'