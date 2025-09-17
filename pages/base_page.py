from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.common.exceptions import (ElementClickInterceptedException,
                                      TimeoutException,
                                      StaleElementReferenceException)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

    def find_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(locator)
        )

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", element)
        time.sleep(0.3)

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.scroll_to_element(element)
        try:
            element.click()
        except (ElementClickInterceptedException, StaleElementReferenceException):
            self.driver.execute_script("arguments[0].click();", element)
        return element

    def input_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
        self.scroll_to_element(element)
        element.send_keys(text)
        return element

    def select_by_visible_text(self, locator, text):
        select_element = self.find_element(locator)
        select = Select(select_element)
        select.select_by_visible_text(text)
        return select_element