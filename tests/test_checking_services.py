from conftest import driver
from pages.login_page import LoginPage
from pages.records_page import RecordsPage
from pages.services_page import ServicesPage
from pages.locators import CommonLocators

def test_checking_services(driver):
    login_page = LoginPage(driver)
    records_page = RecordsPage(driver)
    services_page = ServicesPage(driver)

    login_page.login()
    records_page.records_click()
    records_page.services_click()
    records_page.select_account_click()
    records_page.account_name_click()

    assert services_page.is_button_add_clickable(CommonLocators.BUTTON_ADD), "Кнопка 'Добавить' не кликабельна"
    assert services_page.is_count_rows_service_table() > 0, "Услуг в таблице нет"
