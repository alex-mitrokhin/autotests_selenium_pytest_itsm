import time
from conftest import driver
from pages.login_page import LoginPage
from pages.settings_page import SettingsPage
from pages.surveys_page import SurveysPage
from pages.common_methods import CommonMethods

def test_add_survey(driver):
    login_page = LoginPage(driver)
    common_methods = CommonMethods(driver)
    settings_page = SettingsPage(driver)
    surveys_page = SurveysPage(driver)

    login_page.login()

    common_methods.settings_click()
    common_methods.select_account_click()
    common_methods.account_name_click()

    settings_page.surveys_click()
    common_methods.add_click()
    surveys_page.name_survey_input()
    surveys_page.question_survey_input()
    surveys_page.weight_question_input()
    surveys_page.services_survey_click()
    surveys_page.link_services_click()
    surveys_page.name_service_input()
    surveys_page.name_service_click()
    surveys_page.done_click()
    surveys_page.button_save_click()

    assert surveys_page.get_title_text() == "Опрос_1", "Имя опроса не совпадает"

    time.sleep(2)