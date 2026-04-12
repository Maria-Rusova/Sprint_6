import allure
from ..locators.home_page_locators import HomePageLocators
from ..locators.order_page_locators import OrderPageLocators
from ..pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Прокрутить до элемента страницы')
    def scroll_to_question_about_important_section(self):
        self.scroll_to_element(HomePageLocators.QUESTIONS_ABOUT_IMPORTANT_TITLE)

    @allure.step('Нажать на один вопрос списка')
    def click_question_buttons(self, question_id: int):
        elements = self.find_elements(HomePageLocators.QUESTION_BUTTONS, 10)
        elements[question_id].click()
        self.element_is_visible(HomePageLocators.get_question_id_text(question_id))

    @allure.step('Нажать на логотип "Яндекс"')
    def click_yandex_logo_button(self):
        self.click_element(HomePageLocators.YANDEX_LOGO)

    @allure.step('Нажать на логотип "Самокат"')
    def click_scooter_logo_button(self):
        self.click_element(HomePageLocators.SCOOTER_LOGO)

    def get_question_button_text(self, question_id):
        return self.find_element(HomePageLocators.get_question_button(question_id))

    def scroll_to_order_button(self, order_button):
        self.scroll_to_element(order_button)

    def click_order_button(self, order_button):
        self.click_element(order_button)

    def wait_for_order_header_text(self):
        self.element_is_visible(OrderPageLocators.ORDER_HEADER)