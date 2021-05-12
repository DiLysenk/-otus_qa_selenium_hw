import pytest
from framework import wait_time, assert_element


def test_title(browser):
    wait_time("Your Store", browser)


# 2.1
@pytest.mark.parametrize('selector', ['[href="http://localhost/desktops"]',
                                      '[href="http://localhost/component"]',
                                      '[href="http://localhost/tablet"]',
                                      '[href="http://localhost/software"]',
                                      '.fa.fa-search']
                         )
def test_main_page(browser, selector):
    assert_element(selector, browser)


# 2.2
@pytest.mark.parametrize('selector', ['[for="input-sort"]',
                                      '[for="input-limit"]',
                                      '#compare-total',
                                      '.breadcrumb',
                                      '.img-responsive']
                         )
def test_cataloge(browser, selector):
    browser.get('http://localhost/index.php?route=product/category&path=20')
    assert_element(selector, browser, 3)


# 2.3
@pytest.mark.parametrize('selector', ['.fa.fa-heart',
                                      '.breadcrumb',
                                      '[href="#tab-description"]',
                                      '[href="#tab-review"]',
                                      '.btn.btn-primary.btn-lg.btn-block']
                         )
def test_cataloge(browser, selector):
    browser.get('http://localhost/index.php?route=product/product&path=57&product_id=49')
    assert_element(selector, browser)

# 2.4
@pytest.mark.parametrize('selector', ['.breadcrumb',
                                      '[type="submit"]',
                                      '[value="Login"]',
                                      '[placeholder="E-Mail Address"]',
                                      '[placeholder="Password"]']
                         )
def test_login(browser, selector):
    browser.get('http://localhost/index.php?route=account/login')
    assert_element(selector, browser)

# 2.5
@pytest.mark.parametrize('selector', ['[placeholder="Username"]',
                                      '[placeholder="Password"]',
                                      '[href="http://localhost/admin/index.php?route=common/forgotten"]',
                                      '[type="submit"]',
                                      '[href="http://www.opencart.com"]']
                         )
def test_cataloge(browser, selector):
    browser.get('http://localhost/admin/')
    assert_element(selector, browser)
