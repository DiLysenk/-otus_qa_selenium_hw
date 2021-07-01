import pytest
import logging
import allure
from selenium import webdriver
from pageobject.LoginPage import LoginAdminPage
from ConfigParser import ConfigParser

# DRIVERS = os.path.expanduser("~/Downloads/drivers")

config = ConfigParser()

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    , level=logging.INFO, filename="logs/selenium.log")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption('--headless', action="store_true", help="Run headless")
    parser.addoption('--executor', action="store", help="run remote with arguments + ip")
    parser.addoption('--bversion', action="store", default="90.0", help="version browser")


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    headless = request.config.getoption("--headless")
    bversion = request.config.getoption("--bversion")
    if executor != None:
        caps = {
            "browserName": browser,
            "browserVersion": bversion,
            'goog:chromeOptions': {}
        }
        browser = webdriver.Remote(
            command_executor=f'http://{executor}:4444/wd/hub',
            desired_capabilities=caps
        )
        browser.maximize_window()
        browser.get(config.USER_FRONT)
    elif headless == True:
        options = webdriver.ChromeOptions()
        options.headless = request.config.getoption("--headless")
        browser = webdriver.Chrome(options=options)
        browser.maximize_window()
        browser.get(config.USER_FRONT)
    else:
        browser = webdriver.Chrome()
        browser.maximize_window()

    def fin():
        browser.quit()

    request.addfinalizer(fin)
    return browser

@pytest.fixture(scope='function')
def loging(request, browser):
    logger = logging.getLogger('BrowserLogger')
    test_name = request.node.name

    logger.info(f"===> Test started name, test is {test_name}")

    def fin():
        allure.attach(
            browser.get_screenshot_as_png(),
            name='finalizer attach',
            attachment_type=allure.attachment_type.PNG
        )
        logger.info(f"===> Test finished name, test is {test_name}")

    request.addfinalizer(fin)

