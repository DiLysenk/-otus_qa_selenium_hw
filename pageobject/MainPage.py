from .BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    CURRENCY = (By.CSS_SELECTOR, '.btn.btn-link.dropdown-toggle')
    POUND_STERLING = "£ Pound Sterling"
    CABINET = (By.CSS_SELECTOR, '.hidden-xs.hidden-sm.hidden-md')
    OpenCArt = 'http://localhost/'


    def change_currency(self):
        self.click_element(self.element_css(self.CURRENCY))
        self.click_element(self.element_text(self.POUND_STERLING))

    def forward_to_register(self):
        self.click_element(self.element_css_clickble(self.CABINET))
        self.click_element((self.element_text('Регистрация')))
