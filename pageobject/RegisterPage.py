from .Base import BasePage
from selenium.webdriver.common.by import By
from faker.providers.internet import Provider
fake = Provider(1)


class RegisterPage(BasePage):
    FIRST_NAME = (By.CSS_SELECTOR, '[placeholder="First Name"]')
    LAST_NAME = (By.CSS_SELECTOR, '[placeholder="Last Name"]')
    EMAIL = (By.CSS_SELECTOR, '[placeholder="E-Mail"]')
    TELEPHONE = (By.CSS_SELECTOR, '[placeholder="Telephone"]')
    PASSWORD = (By.CSS_SELECTOR, '[placeholder="Password"]')
    PASSWORD_CONFIRM = (By.CSS_SELECTOR, '[placeholder="Password Confirm"]')
    CHECK_BOX_AGREE = (By.CSS_SELECTOR, '[name="agree"]')
    CONTINUE = (By.CSS_SELECTOR, '[value="Continue"]')

    def fill_form(self):
        self.sending_keys(self.FIRST_NAME, "name")
        self.sending_keys(self.LAST_NAME, "name")
        self.sending_keys(self.EMAIL, "xbend@mail.com")
        self.sending_keys(self.TELEPHONE, "123456789")
        self.sending_keys(self.PASSWORD, "123456")
        self.sending_keys(self.PASSWORD_CONFIRM, "123456")
        return self


    def agree_polycy(self):
        self.click(self.CHECK_BOX_AGREE)
        return self

    def click_continue(self):
        self.click(self.CONTINUE)
