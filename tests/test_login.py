import pytest

from src.pages.login import LoginPage
from src.utils.data import test_password


class TestLogin:
    @pytest.mark.parametrize('email', ['plainaddress', '#@%^%#$@#$@#.com', "@example.com'", "mith <email@example.com>"])
    def test_incorrect_email(self, email, driver):
        page = LoginPage()
        page.login(email, test_password)

        assert page.ALERT.is_displayed()

    def test_login(self, login):
        assert login.text_is_display()
