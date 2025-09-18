from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.common_methods import CommonMethods
from pages.locators import ProjectsPageLocators, RecordsPageLocators, CommonLocators

class ProjectsPage(CommonMethods):

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

    def existing_project_click(self):
        return self.click(ProjectsPageLocators.EXISTING_PROJECT)

    def add_invoice_click(self):
        return self.click(ProjectsPageLocators.BUTTON_ADD_INVOICE)

    def supplier_invoice_input(self, text="ДИТ. Госуслуги Москвы.Внешние подрядчики"):
        return self.input_text(ProjectsPageLocators.INPUT_SUPPLIER_INVOICE, text)

    def supplier_invoice_click(self):
        return self.click(ProjectsPageLocators.BUTTON_SELECT_SUPPLIER)

    def number_invoice_input(self, text=1234):
        return self.input_text(ProjectsPageLocators.INPUT_NUMBER_INVOICE, text)

    def input_date_via_js(self, date_str="15/09/2025"):
        """Установка даты через JavaScript"""
        wait = WebDriverWait(self.driver, 10)
        date_field = wait.until(EC.presence_of_element_located(ProjectsPageLocators.INPUT_DATE_INVOICE))

        # Очистка и установка значения через JS
        self.driver.execute_script("""
            arguments[0].value = '';
            arguments[0].value = arguments[1];
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, date_field, date_str)

        print(f"Дата установлена через JS: {date_str}")

    def unit_price_invoice_input(self, text=1000):
        return self.input_text(ProjectsPageLocators.INPUT_UNIT_PRICE_INVOICE, text)

    def quantity_invoice_input(self, text=20):
        return self.input_text(ProjectsPageLocators.INPUT_QUANTITY_INVOICE, text)

    def get_amount_invoice_text(self):
        amount_invoice = self.find_element(ProjectsPageLocators.AMOUNT_INVOICE)
        print(amount_invoice.text.lstrip('₽ '))
        return amount_invoice.text.lstrip('₽ ')
