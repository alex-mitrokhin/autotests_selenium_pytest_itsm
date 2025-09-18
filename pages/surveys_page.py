from pages.common_methods import CommonMethods
from pages.locators import SettingsPageLocators, SurveysPageLocators

class SurveysPage(CommonMethods):

    def name_survey_input(self, text="Опрос_1"):
        return self.input_text(SurveysPageLocators.INPUT_NAME_SURVEY, text)

    def question_survey_input(self, text="Что такое опрос ?"):
        return self.input_text(SurveysPageLocators.INPUT_QUESTION, text)

    def weight_question_input(self, text=80):
        return self.input_text(SurveysPageLocators.INPUT_WEIGHT, text)

    def services_survey_click(self):
        return self.click(SurveysPageLocators.BUTTON_SERVICES_SURVEY)

    def link_services_click(self):
        return self.click(SurveysPageLocators.BUTTON_LINK_SERVICES)

    def name_service_input(self, text="ПЗПП. СА. Управление инцидентами"):
        return self.input_text(SurveysPageLocators.INPUT_NAME_SERVICE, text)

    def name_service_click(self):
        return self.click(SurveysPageLocators.BUTTON_SELECT_NAME_SERVICE)

    def done_click(self):
        return self.click(SurveysPageLocators.BUTTON_DONE)

    def get_title_text(self):
        status_element = self.find_element(SurveysPageLocators.TITLE_SURVEY)
        return status_element.text




