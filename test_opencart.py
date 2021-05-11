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
    wait_time("Your Store", browser)
    assert_element(selector, browser)


# 2.2
@pytest.mark.parametrize('selector', ['']
                         )
def test_cataloge(browser, selector):
    wait_time(wait_time("Your Store", browser))
    assert_element(selector, browser)

#
# # 2.3
# def test_cart_(browser):
#     pass
#
#
# # 2.4
# def test_login_page(browser):
#     pass
#
#
# # 2.5
# def test_admin_login_page(browser):
#     pass
