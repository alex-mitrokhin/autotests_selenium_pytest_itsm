from selenium.webdriver.common.by import By

class LoginPageLocators:
    USER_EMAIL = (By.ID, 'user_session_email')
    USER_PASSWORD = (By.ID, 'user_session_password')
    EMAIL_BUTTON = (By.ID, 'email-button')
    CONTINUE_BUTTON = (By.ID, 'continue')
    SIGN_IN_BUTTON = (By.ID, 'signin')

class RequestsPageLocators:
    OPEN_REQUEST_FOR_MYSELF = (By.XPATH, '//a[text()="Я хочу открыть заявку для себя"]')

    DOMAIN_GU_MOSCOW_EXT_CONTR = (By.XPATH, '//span[text()="ДИТ. Госуслуги Москвы. Внешние подрядчики"]')
    SERVICE_PZPP = (By.XPATH, '//span[text()="Поддержка ПЗПП"]')
    SERVICE_INSTANCE_PZPP = (By.XPATH, '//span[text()="ПЗПП. ПА. Управление инцидентами ППО"]')
    SELECT_TEMPLATE = (By.XPATH, '//a[text()="ПЗПП. Инциденты ППО"]')

    INPUT_NOTE_REQUEST = (By.CSS_SELECTOR, 'div#req_note')
    DROPDOWN_IMPACT = (By.ID, 'req_impact')
    BUTTON_DESCRIPTION_UI = (By.CSS_SELECTOR, 'li#tab_1')
    INPUT_FIELD_DESCRIPTION = (By.CSS_SELECTOR, 'div#ui-extension_description > div > .ProseMirror')

    BUTTON_DECLINE_REQUEST = (By.CSS_SELECTOR, 'div#toolbar_decline')
    BUTTON_ACCEPT_REQUEST = (By.CSS_SELECTOR, 'div#toolbar_accept')
    BUTTON_START_REQUEST = (By.CSS_SELECTOR, 'div#toolbar_start')
    BUTTON_FORWARD_REQUEST = (By.CSS_SELECTOR, 'div#toolbar_forward')
    BUTTON_COMPLETE_REQUEST = (By.CSS_SELECTOR, 'div#toolbar_complete')

    DROPDOWN_STATUS = (By.ID, 'req_status')
    DROPDOWN_REASON = (By.ID, 'req_completion_reason')

    STATUS_REQUEST = (By.XPATH, '//div[@class="header_bar_section"][4]/div[@class="data"]')
    REQUESTED_FOR = (By.CSS_SELECTOR, 'span[title*="Митрохин"]')

class ProjectsPageLocators:
    INPUT_SUBJECT_PROJECT = (By.CSS_SELECTOR, 'input.title_field')

    INPUT_SERVICE_PROJECT = (By.ID, 'project_service')
    INPUT_PROGRAM_PROJECT = (By.ID, 'project_program')
    INPUT_CUSTOMER_PROJECT = (By.ID, 'project_customer')
    DROPDOWN_JUSTIFICATION_PROJECT = (By.ID, 'project_justification')
    BUTTON_SELECT_PROGRAM_PROJECT = (By.CSS_SELECTOR, 'div.head')
    BUTTON_SELECT_SERVICE_PROJECT = (By.CSS_SELECTOR, 'div.head.strong')
    BUTTON_SELECT_CUSTOMER_PROJECT = (By.XPATH, '//div[@class="head strong"]//span[starts-with(text(), "ДИТ")]')
    PROJECT_STATUS = (By.XPATH, '//div[@class="header_bar_section"][3]/div[@class="data"]')

class RecordsPageLocators:
    BUTTON_REQUESTS = (By.CSS_SELECTOR, 'a[href*="/requests"]')
    BUTTON_REQUEST_TEMPLATES = (By.CSS_SELECTOR, 'a[href*="/request_templates"]')

    BUTTON_WORKFLOWS = (By.CSS_SELECTOR, 'a[href*="/workflows"]')
    BUTTON_WORKFLOW_TEMPLATES = (By.CSS_SELECTOR, 'a[href*="/workflow_templates"]')
    BUTTON_TASK_TEMPLATES = (By.CSS_SELECTOR, 'a[href*="/task_templates"]')
    BUTTON_PROJECTS = (By.CSS_SELECTOR, 'a[href*="/projects"]')

    BUTTON_SERVICES = (By.CSS_SELECTOR, 'a[href*="/services"]')
    BUTTON_SERVICE_INSTANCES = (By.CSS_SELECTOR, 'a[href*="/service_instances"]')
    BUTTON_SERVICE_OFFERINGS = (By.CSS_SELECTOR, 'a[href*="/service_offerings"]')
    BUTTON_SLAS = (By.CSS_SELECTOR, 'a[href*="/slas"]')
    BUTTON_PRODUCTS = (By.CSS_SELECTOR, 'a[href*="/products"]')
    BUTTON_CIS = (By.CSS_SELECTOR, 'a[href=*"/cis"]')
    BUTTON_TEAMS = (By.CSS_SELECTOR, 'a[href*="/teams"]')

class SettingsPageLocators:
    BUTTON_OVERVIEW_ACCOUNT = (By.CSS_SELECTOR, 'a[href*="/overview"]')
    ROWS_ACCOUNT_OVERVIEW = (By.CLASS_NAME, 'row-value')

class ModalWindowLocators:
    BUTTON_MODAL_OK = (By.CSS_SELECTOR, 'div.flash-panel-footer > button[aria-label="OK"]')

class CommonLocators:
    # ===== ЭЛЕМЕНТЫ ПАНЕЛИ ИНСТРУМЕНТОВ СИСТЕМЫ =====
    BUTTON_RECORDS = (By.CLASS_NAME, 'icon-records')
    BUTTON_INBOX = (By.CLASS_NAME, 'icon-inbox')
    BUTTON_SERVICE_DESC = (By.CLASS_NAME, 'icon-service-desk')
    BUTTON_ANALYTICS = (By.CLASS_NAME, 'icon-analytics')
    BUTTON_SETTINGS = (By.CLASS_NAME, 'icon-settings')

    # Элементы выбора пространства (домена)
    BUTTON_SELECT_ACCOUNT = (By.ID, 'account_name')
    BUTTON_ACCOUNT_NAME = (By.CSS_SELECTOR, 'a[href*="/v/sc-gu/"]')

    # Элементы на верхней панели
    BUTTON_ADD = (By.CSS_SELECTOR, 'div#toolbar_add')
    BUTTON_EDIT = (By.CSS_SELECTOR, 'div#toolbar_edit')
    BUTTON_ACTIONS = (By.CSS_SELECTOR, 'div#toolbar_actions')

    BUTTON_SAVE = (By.ID, 'save')