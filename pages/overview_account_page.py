from pages.common_methods import CommonMethods
from pages.locators import SettingsPageLocators, CommonLocators

class OverviewAccountPage(CommonMethods):

    def overview_account_click(self):
        return self.click(SettingsPageLocators.BUTTON_OVERVIEW_ACCOUNT)

    def check_row_values(self):
        elements = self.find_elements(SettingsPageLocators.ROWS_ACCOUNT_OVERVIEW)

        indexes_to_skip = [2, 11]

        # Используем словарь {индекс: ожидаемое_значение}
        expected_values = {
            0: "sc-gu",
            1: "https://sc-gu.itsm-qa.mos.ru",
            3: "Премиум",
            4: "Служебная УЗ",
            5: "ДИТ. Госуслуги Москвы. Внешние подрядчики",
            6: "RUB Российский рубль",
            7: "Русский",
            8: "Москва",
            9: "24-часа (15:00)",
            10: "Каталог услуг Правительства Москвы"
        }

        for i, element in enumerate(elements):
            if i in indexes_to_skip:
                print(f"Пропускаем проверку элемента {i + 1} (индекс {i})")
                continue

            if i in expected_values:  # Проверяем есть ли индекс в словаре
                expected = expected_values[i]  # Получаем значение по ключу-индексу
                actual_text = element.text.strip('₽').strip()
                assert actual_text == expected, \
                    f"Элемент {i + 1}: ожидалось '{expected}', получено '{actual_text}'"

