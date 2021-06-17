import pytest
import os
from selenium import webdriver


DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        choices=["chrome", "firefox", "opera"],
        default="chrome"
    )
    parser.addoption(
        "--uurl",
        default="http://localhost/"
    )


@pytest.fixture(scope='session')
def browser(request):
    browser = request.config.getoption("--browser")
    common_caps = {"pageLoadStrategy": "eager"}
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=f'{DRIVERS}/chromedriver',
                                  desired_capabilities=common_caps
                                  )
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f'{DRIVERS}/geckodriver')
    elif browser == 'opera':
        driver = webdriver.Opera(executable_path=f'{DRIVERS}/operadriver')
    else:
        raise ValueError(f"Driver not supported: {browser}")  # исключение для неизветсного параметра
    url = request.config.getoption('--uurl')
    driver.get(url)
    request.addfinalizer(driver.quit)
    return driver
