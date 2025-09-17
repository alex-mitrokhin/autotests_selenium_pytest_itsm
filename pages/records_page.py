from pages.base_page import BasePage
from pages.common_methods import CommonMethods
from pages.locators import RecordsPageLocators, CommonLocators

class RecordsPage(CommonMethods):

    def records_click(self):
        return self.click(CommonLocators.BUTTON_RECORDS)

    def requests_click(self):
        return self.click(RecordsPageLocators.BUTTON_REQUESTS)

    def select_account_click(self):
        return self.click(CommonLocators.BUTTON_SELECT_ACCOUNT)

    def account_name_click(self):
        return self.click(CommonLocators.BUTTON_ACCOUNT_NAME)

    def requested_for_click(self):
        return self.click(RecordsPageLocators.REQUESTED_FOR)

    def edit_req_click(self):
        return self.click(CommonLocators.BUTTON_EDIT)