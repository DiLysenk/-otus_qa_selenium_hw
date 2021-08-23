from selenium.webdriver.common.by import By
from ConfigParser import ConfigParser
from .BasePage import BasePage

configparser = ConfigParser()


class LoginAdminPage(BasePage):
    USERNAME_ADMIN = (By.CSS_SELECTOR, '[name="username"]')
    PASSWORD_ADMIN = (By.CSS_SELECTOR, '[name="password"]')
    LOGIN_BUTTON_ADMIN = (By.CSS_SELECTOR, ".btn.btn-primary")
    ADMIN_PAGE = 'https://demo.opencart.com/admin/'

    def login_admin(self):
        self.input_keys(self.element_css(self.USERNAME_ADMIN), configparser.LOGIN)
        self.input_keys(self.element_css(self.PASSWORD_ADMIN), configparser.PASSWORD)
        self.click_element(self.element_css_clickble(self.LOGIN_BUTTON_ADMIN))
