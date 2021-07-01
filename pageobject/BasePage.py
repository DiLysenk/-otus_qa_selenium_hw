import logging
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:  # базовый класс для PageObject

    def __init__(self, browser, wait=5):  # инициализация браузера
        self.browser = browser
        self.wait = WebDriverWait(self.browser, wait)
        self.logger = logging.getLogger(type(self).__name__)


    # метод для верификации ссылки с помощью текста
    def _verify_link_presence(self, link_text):
        try:
            self.wait.until(lambda driver: self.browser.execute_script('return document.readyState') == 'complete')
            element = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.logger.info(f" найден элемент с ссылкой {link_text}")
            return element
        except TimeoutException:
            self.logger.info(f"элемент не найден {link_text}")
            raise AssertionError(f"Не могу найти по элемент по ссылке: {link_text}")

    # метод для верификации элемента с помощью селектора
    def _verify_element_presence(self, locator: tuple):
        try:
            self.wait.until(lambda driver: self.browser.execute_script('return document.readyState') == 'complete')
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.logger.info(f" найден элемент с локатором {locator}")
            return element
        except TimeoutException:
            self.logger.info(f"элемент не найден {locator}")
            raise AssertionError(f"не могу найти элемент по локатору: {locator}")

    # метод для верификации элемента с помощью текста
    def _verify_element_by_text(self, text: str):
        try:
            self.wait.until(lambda driver: self.browser.execute_script('return document.readyState') == 'complete')
            element = self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//*[text()='{text}']")))
            self.logger.info(f" найден элемент с текстом {text}")
            return element
        except TimeoutException:
            self.logger.info(f"элемент не найден {text}")
            raise AssertionError(f"не могу найти элемент по тексту: {text}")

    # метод для верификации элементов с помощью текста
    def _verify_elements_presence(self, locator: tuple, quantity: int = 1):
        try:
            self.wait.until(lambda driver: self.browser.execute_script('return document.readyState') == 'complete')
            if len(self.wait.until(EC.visibility_of_all_elements_located(locator))) >= quantity:
                return self.wait.until(EC.visibility_of_all_elements_located(locator))
            else:
                self.wait_time(3)
                return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.info(f"элемент не найден {locator}")
            raise AssertionError(f"не могу найти элементы по локатору: {locator}")

    # метод для верификации элемента с помощью CSS на кликабельность
    def _verify_element_clicable(self, locator: tuple):
        try:
            self.wait.until(lambda driver: self.browser.execute_script('return document.readyState') == 'complete')
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.logger.info(f" найден элемент с кликаббельным локаттором {locator}")
            return element
        except TimeoutException:
            self.logger.info(f"элемент не найден {locator}")
            raise AssertionError(f"Элемент не становится кликабельным: {locator}")

    def _verify_element_out(self, locator: tuple):
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            self.logger.info(f"элемент не найден {locator}")
            self.browser.save_screenshot(f"././screen/{locator}.png")
            raise AssertionError(f"элемент не исчез с экрана {locator}")

    def _verify_url(self, url):
        try:
            return self.wait.until(EC.url_to_be(url))
        except TimeoutException:
            self.logger.info(f"адрес странички не  {url}")
            self.browser.save_screenshot(f"././screen/{url}.png")
            raise AssertionError(f"некорректный адрес страницчки {url}")

    def element_css_out(self, locator: tuple):
        return self._verify_element_out(locator)

    def elements_css(self, locator: tuple, quantity: int = 1):
        return self._verify_elements_presence(locator, quantity)

    def element_css_clickble(self, locator: tuple):
        return self._verify_element_clicable(locator)

    # клик с помощью экшон чейнс
    def click_element_ac(self, element):
        ActionChains(self.browser).pause(0.1).move_to_element(element).click().perform()

    def element_css(self, locator: tuple):
        return self._verify_element_presence(locator)

    def element_text(self, text: str):
        return self._verify_element_by_text(text)

    def element_linktext(self, link: str):
        return self._verify_link_presence(link)

    def click_element(self, element):
        self.logger.info(f"Clicking element")
        element.click()

    def click_in_element(self, element, locator: tuple, index: int = 0):
        self.logger.info("Clicking element")
        element = element.find_elements(*locator)[index]
        self.click_element(element)

    def input_keys(self, element, text):
        self.logger.info(f"input text {text}")
        element.send_keys(text)

    def browser(self):
        return self.browser.current_url


    def get_atribute_element(self, element, attribute):
        return element.get_attribute(attribute)

    def browser_refresh(self):
        self.browser.refresh()
        self.wait_time(1)
        self.element_css((By.CSS_SELECTOR, "html"))

    def get_text_of_element(self, element):
        return element.get_property('textContent')

    def get_html_of_element(self, element):
        return element.get_property('outerHTML')

    def wait_time(self, time: int = 1):
        sleep(time)
        return self

    def foward_to_screen(self, text: str):
        self.click_element(self.element_linktext(text))
        return self

    def forward_to_url(self, url):
        self.browser.get(url)
        return self
