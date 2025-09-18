from conftest import driver
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from pages.overview_account_page import OverviewAccountPage
from pages.common_methods import CommonMethods

def test_overview_account(driver):
    login_page = LoginPage(driver)
    common_methods = CommonMethods(driver)
    settings_page = SettingsPage(driver)
    overview_account_page = OverviewAccountPage(driver)

    login_page.login()

    common_methods.settings_click()
    common_methods.select_account_click()
    common_methods.account_name_click()

    settings_page.overview_account_click()
    overview_account_page.check_row_values()
