from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.common_methods import CommonMethods
from pages.locators import ServicesPageLocators

class ServicesPage(CommonMethods):

    def is_count_rows_service_table(self):
        rows_in_table = self.find_elements(ServicesPageLocators.ROWS_SERVICE_TABLE)
        return len(rows_in_table)

