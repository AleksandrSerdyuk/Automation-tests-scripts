from src.pages.locators import LoginLocators
from src.webelements.button import Button, Element
from src.webelements.input_field import InputField
from src.pages.base import BasePage


class LoginPage(BasePage):
    EMAIL_FIELD = InputField(LoginLocators.EMAIL_FIELD)
    PASSWORD_FIELD = InputField(LoginLocators.PASSWORD_FIELD)
    ALERT = Element(LoginLocators.PASSWORD_FIELD)
    CONFIRM_TEXT = Element(LoginLocators.CONFIRM_TEXT)
    LOGIN_BUTTON = Button(LoginLocators.LOG_IN_BUTTON)

    def is_opened(self):
        return self.LOGIN_BUTTON.is_displayed()

    def login(self, email, password):
        self.EMAIL_FIELD.set_text(email)
        self.PASSWORD_FIELD.set_text(password)
        self.LOGIN_BUTTON.click()

    def text_is_display(self):
        return self.CONFIRM_TEXT.wait_for_visibility()
