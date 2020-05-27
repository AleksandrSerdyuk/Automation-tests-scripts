from selenium.webdriver.common.by import By


class LoginLocators:

    EMAIL_FIELD = (By.CSS_SELECTOR, '#login')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#password')
    LOG_IN_BUTTON = (By.CSS_SELECTOR, '#sign-in-form > button')
    ALERT = (By.CSS_SELECTOR, '#sign-in-form > div.field.error > div')
    CONFIRM_TEXT = (By.CSS_SELECTOR, '#email-verification-message')
