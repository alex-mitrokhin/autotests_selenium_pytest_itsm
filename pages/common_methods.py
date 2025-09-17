from pages.base_page import BasePage
from pages.locators import ModalWindowLocators, CommonLocators, RequestsPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException

class CommonMethods(BasePage):
    def service_desk_click(self):
        return self.click(CommonLocators.BUTTON_SERVICE_DESC)

    def records_click(self):
        return self.click(CommonLocators.BUTTON_RECORDS)

    def settings_click(self):
        return self.click(CommonLocators.BUTTON_SETTINGS)

    def select_account_click(self):
        return self.click(CommonLocators.BUTTON_SELECT_ACCOUNT)

    def account_name_click(self):
        return self.click(CommonLocators.BUTTON_ACCOUNT_NAME)

    def add_click(self):
        return self.click(CommonLocators.BUTTON_ADD)

    def edit_click(self):
        return self.click(CommonLocators.BUTTON_EDIT)

    def button_save_click(self):
        return self.click(CommonLocators.BUTTON_SAVE)

    def processing_modal_window(self):
        try:
            modal_window = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(ModalWindowLocators.BUTTON_MODAL_OK)
            )
            print("Модальное окно появилось, нажимаем OK...")
            self.driver.execute_script("arguments[0].click();", modal_window)
            WebDriverWait(self.driver, 5).until(
                EC.invisibility_of_element_located(ModalWindowLocators.BUTTON_MODAL_OK)
            )
            print("Модальное окно закрыто.")
            return True
        except TimeoutException:
            print("Модальное окно не появилось, продолжаем выполнение.")
            return False

    def wait_for_ajax_complete(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script(
                    'return (typeof jQuery !== "undefined") ? jQuery.active == 0 : true'
                )
            )
            print("AJAX-запросы завершены.")
        except Exception as e:
            print(f"AJAX-запросы не завершились: {e}")

    def complete_save_operation(self):
        """Оптимизированный процесс сохранения с повторными попытками"""

        max_attempts = 2  # Уменьшим до 2 попыток, так как этого достаточно

        for attempt in range(max_attempts):

            try:
                self.button_save_click()
                self.processing_modal_window()
                self.wait_for_ajax_complete()

                # Проверяем наличие статуса
                try:
                    status_element = WebDriverWait(self.driver, 2).until(
                        EC.visibility_of_element_located(RequestsPageLocators.STATUS_REQUEST)
                    )
                    print("Элемент статуса найден и видим")
                    return status_element

                except TimeoutException:
                    if attempt < max_attempts - 1:
                        print("Элемент статуса не найден, пробуем снова...")
                    else:
                        print("Элемент статуса не найден после всех попыток")
                        raise

            except Exception as e:
                print(f"Ошибка в попытке {attempt + 1}: {e}")
                if attempt == max_attempts - 1:
                    raise

    def wait_for_text_in_element(self, locator, text, timeout=10):
        """Ожидание определенного текста в элементе"""
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )