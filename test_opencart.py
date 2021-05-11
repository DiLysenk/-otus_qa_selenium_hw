from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_title(browser):
    WebDriverWait(browser, 1).until(EC.title_is('Your Store'))


# 2.1
@pytest.mark.parametrize('selector', ['[href="http://localhost/desktops"]',
                                      '[href="http://localhost/component"]',
                                      '[href="http://localhost/tablet"]'],
                         '[href="http://localhost/software"]',
                         '[.fa.fa-search]'
                         )
def test_main_page(browser, selector):
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))


# 2.2
@pytest.mark.parametrize('selector', ['']
                         )
def test_cataloge(browser):
    WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))


# 2.3
def test_cart_(browser):
    pass


# 2.4
def test_login_page(browser):
    pass


# 2.5
def test_admin_login_page(browser):
    pass
