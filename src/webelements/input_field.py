from .element import Element


class InputField(Element):

    def set_text(self, text):
        self.clear().send_keys(text)

    def clear(self):

        self.wait_for_visibility()
        self.web_element.clear()
        return self

    def send_keys(self, text):

        self.wait_for_visibility()
        self.web_element.send_keys(text)
        return self
