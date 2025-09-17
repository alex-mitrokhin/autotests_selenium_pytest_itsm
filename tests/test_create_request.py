from conftest import driver
from pages.login_page import LoginPage
from pages.requests_page import RequestsPage
from pages.records_page import RecordsPage


def test_request_creation(driver):
    login_page = LoginPage(driver)
    records_page = RecordsPage(driver)
    requests_page = RequestsPage(driver)

    login_page.login()
    records_page.records_click()
    records_page.requests_click()
    records_page.select_account_click()
    records_page.account_name_click()

    # Создание заявки
    requests_page.service_desk_click()
    requests_page.open_request_for_myself_click()
    requests_page.select_domain_gu_moscow_ext_click()
    requests_page.select_service_click()
    requests_page.select_service_instance_click()
    requests_page.select_template_click()
    requests_page.note_request_input("Тестовый комментарий")
    requests_page.select_impact()
    requests_page.description_ui_click()
    requests_page.description_input("Описание")

    # Сохранение
    status_element = requests_page.complete_request_save()
    assert requests_page.get_status_text() == 'Назначено'