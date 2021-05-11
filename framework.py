from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def wait_time(title, driver, timeout=3):
    try:
        WebDriverWait(driver, timeout).until((EC.title_is(title)))
    except TimeoutException:
        raise AssertionError(f"Не было элемента{title}")


def assert_element(selector, driver, timeout=1):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    except TimeoutException:
        driver.save_screenshon(f"{driver.session_id}.png")
        raise AssertionError(f'{selector}')
