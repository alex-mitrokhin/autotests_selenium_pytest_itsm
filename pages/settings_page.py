from pages.common_methods import CommonMethods
from pages.locators import SettingsPageLocators

class SettingsPage(CommonMethods):

    def overview_account_click(self):
        return self.click(SettingsPageLocators.BUTTON_OVERVIEW_ACCOUNT)

    def surveys_click(self):
        return self.click(SettingsPageLocators.BUTTON_SURVEYS)