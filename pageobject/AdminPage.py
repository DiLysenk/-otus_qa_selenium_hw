from selenium.webdriver.common.by import By
from .BasePage import BasePage


class AdminPage(BasePage):
    CATALOG = (By.CSS_SELECTOR, '[data-toggle="collapse"]')
    PRODUCTS = (By.CSS_SELECTOR, '.collapse.in li + li a')
    ADD_NEW = (By.CSS_SELECTOR, '[data-original-title="Add New"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '[placeholder="Product Name"]')
    META_TAG_TITLE = (By.CSS_SELECTOR, '[placeholder="Meta Tag Title"]')
    MODEL = (By.CSS_SELECTOR, '[placeholder="Model"]')
    SAVE = (By.CSS_SELECTOR, '.fa.fa-save')
    SELECT_PRODUCT = (By.CSS_SELECTOR, '[type="checkbox"]')
    DELETE = (By.CSS_SELECTOR, '.fa.fa-trash-o')
    TABLE = (By.CSS_SELECTOR, '.table.table-bordered.table-hover')
    SUCCESS_DELETE = (By.CSS_SELECTOR, '.alert.alert-success.alert-dismissible')

    def go_to_Products(self):
        self.click_element(self.element_css_clickble(self.CATALOG))
        self.click_element(self.element_css_clickble(self.PRODUCTS))
        return self

    def add_product(self, model):
        self.click_element(self.element_css_clickble(self.ADD_NEW))
        self.input_keys(self.element_css(self.PRODUCT_NAME), model)
        self.input_keys(self.element_css(self.META_TAG_TITLE), model)
        self.click_element(self.element_text('Data'))
        self.input_keys(self.element_css(self.MODEL), model)
        self.click_element(self.element_css_clickble(self.SAVE))
        return self

    def select_product(self):
        self.click_in_element(self.element_css(self.TABLE), self.SELECT_PRODUCT, 2)
        return self

    def delete_product(self):
        self.click_element(self.element_css(self.DELETE))
        alert = self.browser.switch_to.alert
        alert.accept()
