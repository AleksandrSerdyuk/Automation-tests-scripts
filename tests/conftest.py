import pytest

from src.webdriver.driver import web_driver
from src.utils.data import site_url, test_login, test_password
from src.pages.login import LoginPage


driver_state = None


@pytest.yield_fixture(scope="session")
def driver():
    global driver_state
    if not driver_state:
        driver_state = web_driver.start(site_url)
    yield driver_state
    web_driver.quit()


@pytest.yield_fixture()
def login(driver):
    page = LoginPage()
    page.login(test_login, test_password)
    yield page


