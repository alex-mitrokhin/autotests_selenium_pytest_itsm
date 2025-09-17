from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from data.config import Config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage(BasePage):

    def open_url(self):
        self.driver.get(Config.BASE_URL)

    def email_click(self):
        return self.click(LoginPageLocators.EMAIL_BUTTON)

    def email_input(self):
        return self.input_text(LoginPageLocators.USER_EMAIL, Config.USER_EMAIL)

    def continue_click(self):
        return self.click(LoginPageLocators.CONTINUE_BUTTON)

    def password_input(self):
        return self.input_text(LoginPageLocators.USER_PASSWORD, Config.PASSWORD)

    def sign_in_click(self):
        return self.click(LoginPageLocators.SIGN_IN_BUTTON)

    def title_contains(self):
        return WebDriverWait(self.driver, 10).until(
            EC.title_contains('Мои входящие | ДИТ. Сервис-менеджер')
        )

    def login(self):
        """Полный процесс логина"""
        self.open_url()
        self.email_click()
        self.email_input()
        self.continue_click()
        self.password_input()
        self.sign_in_click()
        assert self.title_contains(), 'Логин не выполнен!'
        print("Логин выполнен успешно")
        return self