from .Base import BasePage
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

    def fill_form(self, name, email):
        self.input_keys(self.element(self.FIRST_NAME), name)
        self.input_keys(self.element(self.LAST_NAME), name)
        self.input_keys(self.element(self.EMAIL), email)
        self.input_keys(self.element(self.TELEPHONE), "123456789")
        self.input_keys(self.element(self.PASSWORD), "123456")
        self.input_keys(self.element(self.PASSWORD_CONFIRM), "123456")
        return self

    def agree_polycy(self):
        self.click(self.CHECK_BOX_AGREE)
        return self

    def click_continue(self):
        self.click(self.CONTINUE)
