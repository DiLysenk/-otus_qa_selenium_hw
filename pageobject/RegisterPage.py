from .BasePage import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, '[placeholder="First Name"]')
    LAST_NAME = (By.CSS_SELECTOR, '[placeholder="Last Name"]')
    EMAIL = (By.CSS_SELECTOR, '[placeholder="E-Mail"]')
    TELEPHONE = (By.CSS_SELECTOR, '[placeholder="Telephone"]')
    PASSWORD = (By.CSS_SELECTOR, '[placeholder="Password"]')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '[placeholder="Password Confirm"]')
    CHECK_BOX_AGREE = (By.CSS_SELECTOR, '[name="agree"]')
    CONTINUE = (By.CSS_SELECTOR, '[value="Continue"]')
    URL_REGISTER = 'https://demo.opencart.com/index.php?route=account/register'


    def fill_form(self, name, email):
        self.input_keys(self.element_css(self.FIRST_NAME), name)
        self.input_keys(self.element_css(self.LAST_NAME), name)
        self.input_keys(self.element_css(self.EMAIL), email)
        self.input_keys(self.element_css(self.TELEPHONE), "123456789")
        self.input_keys(self.element_css(self.PASSWORD), "123456")
        self.input_keys(self.element_css(self.PASSWORD_CONFIRM), "123456")
        return self

    def agree_polycy(self):
        self.click_element(self.element_css_clickble(self.CHECK_BOX_AGREE))
        return self

    def click_continue(self):
        self.click_element(self.element_css(self.CONTINUE))
