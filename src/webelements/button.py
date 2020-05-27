from .element import Element


class Button(Element):

    def click(self):

        self.wait_for_visibility()
        self.web_element.click()
