import pytest
from selenium import webdriver


@pytest.fixture
def start_browser(url):
    wd = webdriver.Chrome()
    wd.get(url)



