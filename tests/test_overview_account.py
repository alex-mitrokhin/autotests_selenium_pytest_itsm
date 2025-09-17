from conftest import driver
from pages.login_page import LoginPage
from pages.overview_account_page import OverviewAccountPage
from pages.records_page import RecordsPage

def test_request_creation(driver):
    login_page = LoginPage(driver)
    records_page = RecordsPage(driver)
    overview_account_page = OverviewAccountPage(driver)

    login_page.login()

    overview_account_page.settings_click()
    records_page.select_account_click()
    records_page.account_name_click()

    overview_account_page.overview_account_click()
    overview_account_page.check_row_values()
