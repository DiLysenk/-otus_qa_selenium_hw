from .Base import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    CURRENCY = (By.CSS_SELECTOR, '.btn.btn-link.dropdown-toggle')
    POUND_STERLING = "£ Pound Sterling"


    def change_currency(self):
        self.simple_click_element(self.element(self.CURRENCY))
        self.simple_click_element(self.element_text(self.POUND_STERLING))




