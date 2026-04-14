import allure
from ..urls import Urls
from ..locators.home_page_locators import HomePageLocators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec



class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на страницу')
    def navigate(self, page_url: str = Urls.YA_HOME_PAGE):
        self.driver.get(page_url)

    @allure.step('Получить текущий URL страницы')
    def current_url(self):
        return self.driver.current_url.rstrip('/')

    def find_element(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
        ec.presence_of_element_located(locator),
        f"Can't find element by locator {locator}"
    )

    def find_elements(self, locator: tuple[str, str], timeout: int = 10):
        return WebDriverWait(self.driver, timeout).until(
        ec.presence_of_all_elements_located(locator)
    )

    def click_element(self, locator: tuple[str, str], timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.click()

    def enter_text(self, locator: tuple[str, str], text: str, timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        
    def element_is_visible(self, locator: tuple[str, str], timeout: int = 10) -> bool:              #  
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))
        return True

    def scroll_to_element(self, locator: tuple[str, str], timeout: int = 10):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.find_element(locator))
        self.element_is_visible(locator, timeout)

    @allure.step('Принять cookie')
    def accept_cookies(self):
        self.click_element(HomePageLocators.ACCEPT_COOKIES_BUTTON)

    @allure.step('Нажать Enter для завершения выбора')
    def press_enter_button(self, locator: tuple[str, str], timeout: int = 10):
        self.find_element(locator, timeout).send_keys(Keys.ENTER)

    @allure.step('Переключить вкладку по номеру')
    def switch_to(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Дождаться отображения URL страницы')
    def wait_for_url(self, timeout: int = 10):
        WebDriverWait(self.driver, timeout).until_not(ec.url_matches('about:blank'))