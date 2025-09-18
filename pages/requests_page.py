from pages.common_methods import CommonMethods
from pages.locators import RequestsPageLocators

class RequestsPage(CommonMethods):

    def open_request_for_myself_click(self):
        return self.click(RequestsPageLocators.OPEN_REQUEST_FOR_MYSELF)

    def select_domain_gu_moscow_ext_click(self):
        return self.click(RequestsPageLocators.DOMAIN_GU_MOSCOW_EXT_CONTR)

    def select_service_click(self):
        return self.click(RequestsPageLocators.SERVICE_PZPP)

    def select_service_instance_click(self):
        return self.click(RequestsPageLocators.SERVICE_INSTANCE_PZPP)

    def select_template_click(self):
        return self.click(RequestsPageLocators.SELECT_TEMPLATE)

    def note_request_input(self, text="Комментарий"):
        return self.input_text(RequestsPageLocators.INPUT_NOTE_REQUEST, text)

    def select_impact(self):
        return self.select_by_visible_text(
            RequestsPageLocators.DROPDOWN_IMPACT,
            "Низкое - ухудшение услуги для одного пользователя"
        )

    def description_ui_click(self):
        return self.click(RequestsPageLocators.BUTTON_DESCRIPTION_UI)

    def description_input(self, text="Комментарий"):
        return self.input_text(RequestsPageLocators.INPUT_FIELD_DESCRIPTION, text)

    def accept_request(self):
        return self.click(RequestsPageLocators.BUTTON_ACCEPT_REQUEST)

    def start_request(self):
        return self.click(RequestsPageLocators.BUTTON_START_REQUEST)

    def complete_request(self):
        return self.click(RequestsPageLocators.BUTTON_COMPLETE_REQUEST)

    def select_status_dropdown(self):
        return self.select_by_visible_text(RequestsPageLocators.DROPDOWN_STATUS, "Завершено")

    def select_reason_dropdown(self):
        return self.select_by_visible_text(RequestsPageLocators.DROPDOWN_REASON, "Решено - анализ не требуется")

    def get_status_text(self):
        status_element = self.find_element(RequestsPageLocators.STATUS_REQUEST)
        return status_element.text

    def wait_for_status(self, expected_status, timeout=15):
        try:
            self.wait_for_text_in_element(RequestsPageLocators.STATUS_REQUEST, expected_status, timeout)
            print(f"Статус успешно изменился на: {expected_status}")
            return True
        except Exception:
            print(f"Статус не изменился на: {expected_status} в течение {timeout} секунд")
            return False

    def requested_for_click(self):
        return self.click(RequestsPageLocators.REQUESTED_FOR)