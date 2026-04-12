import pytest
from typing import Generator
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture()
def driver() -> Generator[WebDriver, None, None]:
    driver = webdriver.Firefox()
    yield driver
    driver.quit()