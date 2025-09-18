from pages.common_methods import CommonMethods
from pages.locators import RecordsPageLocators

class RecordsPage(CommonMethods):
    def requests_click(self):
        return self.click(RecordsPageLocators.BUTTON_REQUESTS)

    def projects_click(self):
        return self.click(RecordsPageLocators.BUTTON_PROJECTS)

    def services_click(self):
        return self.click(RecordsPageLocators.BUTTON_SERVICES)

    def service_instances_click(self):
        return self.click(RecordsPageLocators.BUTTON_SERVICE_INSTANCES)

    def service_offerings_click(self):
        return self.click(RecordsPageLocators.BUTTON_SERVICE_OFFERINGS)

    def slas_click(self):
        return self.click(RecordsPageLocators.BUTTON_SLAS)



