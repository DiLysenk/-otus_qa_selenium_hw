from selenium.webdriver.common.by import By

from .Base import BasePage


class LoginAdminPage(BasePage):
    USERNAME_ADMIN = (By.CSS_SELECTOR, '[name="username"]')
    PASSWORD_ADMIN = (By.CSS_SELECTOR, '[name="password"]')
    LOGIN_BUTTON_ADMIN = (By.CSS_SELECTOR, ".btn.btn-primary")

    def login_admin(self):
        self.input_keys(self.element(self.USERNAME_ADMIN), 'user')
        self.input_keys(self.element(self.PASSWORD_ADMIN), 'bitnami')
        self.simple_click_element(self.element(self.LOGIN_BUTTON_ADMIN))
