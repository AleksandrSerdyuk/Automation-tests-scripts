import functools

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from src.webdriver.driver import web_driver

_DEFAULT_TIMEOUT = 30
_TIMEOUT_MESSAGE = 'Could not wait for {} of element. Tried for {} seconds'


def catch_errors(miss=()):
    def catcher_wrapper(func):
        @functools.wraps(func)
        def catcher(obj, catch=True, *args, **kwargs):
            if catch:
                try:
                    return func(obj, *args, **kwargs)
                except Exception as e:
                    if e.__class__ in miss:
                        raise e
                    print('HANDLING AN EXCEPTION ', e)
                    return False
            else:
                return func(obj, *args, **kwargs)

        return catcher

    return catcher_wrapper


class Element:

    def __init__(self, locator=None, parent=None, web_element=None):
        if locator is None and web_element is None:
            raise ValueError('Locator or WebElement must be passed as argument')
        self._locator = locator
        self._parent = parent
        self._web_element = web_element

    @property
    def _driver(self):
        if not hasattr(self, 'driver_obj'):
            driver = web_driver.driver
            if driver is None:
                raise Exception('web_driver.driver is None')
            setattr(self, 'driver_obj', driver)
        return self.__dict__['driver_obj']

    def _wait(self, timeout: int = _DEFAULT_TIMEOUT) -> WebDriverWait:
        return WebDriverWait(self._driver, timeout)

    @property
    def _finder(self):
        return self._parent or self._driver

    @property
    def web_element(self):
        return self.__wait_web_element_dynamically()

    def __wait_web_element_dynamically(self, timeout=_DEFAULT_TIMEOUT):

        element = None
        if self._locator:
            self._wait(timeout).until(lambda _: self.is_present(),
                                      message=f'Could not wait for element with locator {self._locator} to be present')
            element = self._finder.find_element(*self._locator)

        elif self._web_element:
            self._wait(timeout).until(ec.visibility_of(self._web_element),
                                      message=f'Could not wait for visibility element {self._web_element.id}')
            element = self._web_element
        self.scroll_into_view(element)
        return element

    def wait_for_visibility(self, message=None, timeout=_DEFAULT_TIMEOUT):
        return self._wait(timeout).until(lambda _: self.is_displayed(),
                                         message=message or _TIMEOUT_MESSAGE.format('visibility', f'{timeout}'))

    def find_element(self, by: By, value: str):
        self._wait().until(lambda _: self.web_element.find_element(by, value).is_displayed(),
                           f'Could not wait for child element with locator ({by}, {value})')
        return self.web_element.find_element(by, value)

    def find_elements(self, by: By, value: str):
        self._wait().until(lambda _: self.web_element.find_element(by, value).is_displayed(),
                           f'Could not wait for child elements with locator ({by}, {value})')
        return self.web_element.find_elements(by, value)

    @property
    def text(self):
        return self.web_element.text

    @catch_errors()
    def is_enabled(self):
        if self._web_element:
            return self._web_element.is_enabled()
        else:
            return self._finder.find_element(*self._locator).is_enabled()

    @catch_errors()
    def is_displayed(self):
        if self._web_element:
            return self._web_element.is_displayed()
        else:
            self._finder.find_element(*self._locator).is_displayed()
            return True

    @catch_errors()
    def is_present(self):
        if self._web_element:
            return self._web_element.is_displayed()
        else:
            self._finder.find_element(*self._locator)
            return True

    def scroll_into_view(self, element=None):

        target_element = element or self.web_element
        web_driver.driver.execute_script("arguments[0].scrollIntoView();", target_element)
