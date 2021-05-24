from selenium.webdriver.common.by import By

from .Base import BasePage

class LoginPage(BasePage):

    PASSWORD = (By.CSS_SELECTOR, '[placeholder="Password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[value="Login"]')


