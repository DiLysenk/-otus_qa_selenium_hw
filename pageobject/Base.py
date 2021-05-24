from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    # проверка доступности элемента по тексту
    def _verify_link_presence(self, link_text):
        try:
            return WebDriverWait(self.browser, 2) \
                .until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
        except TimeoutException:
            raise AssertionError("Cant find element by link text: {}".format(link_text))

    # проверка доступности элемента по локатору
    def _verify_element_presence(self, locator: tuple):
        try:
            return WebDriverWait(self.browser, 2).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError("Cant find element by locator: {}".format(locator))

    #
    def _element(self, locator: tuple):
        return self._verify_element_presence(locator)

    # клик настоящий
    def _click_element(self, element):
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    # клик обычный
    def simple_click_element(self, element):
        element.click()

    # клик с проверкой элемента
    def click(self, locator: tuple):
        element = self._element(locator)
        ActionChains(self.browser).pause(0.3).move_to_element(element).click().perform()

    # клик в 3 по счёту элемент
    def click_in_element(self, element, locator: tuple, index: int = 0):
        element = element.find_elements(*locator)[index]
        self._click_element(element)

    # Клик по названию элемента
    def click_link(self, link_text):
        self.click((By.LINK_TEXT, link_text))
        return self

    def verify_element_presence(self, locator: tuple):
        return self._verify_element_presence(locator)


    def sending_keys(self, locator: tuple, text):
        return self._element(locator).send_keys(text)
