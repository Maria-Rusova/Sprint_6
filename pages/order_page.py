import allure
#import re
from ..locators.order_page_locators import OrderPageLocators
from ..pages.home_page import HomePage
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support.wait import WebDriverWait
#from selenium.webdriver.support import expected_conditions  # as ec


class OrderPage(HomePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввод имени')
    def input_name(self, name: str):
        self.enter_text(OrderPageLocators.NAME_FIELD, name)

    @allure.step('Ввод фамилии')
    def input_surname(self, surname: str):
        self.enter_text(OrderPageLocators.SURNAME_FIELD, surname)

    @allure.step('Ввод адреса')
    def input_address(self, address: str):
        self.enter_text(OrderPageLocators.ADDRESS_FIELD, address)

    @allure.step('Ввод станции метро')
    def input_subway_station(self, station: str):
        self.find_element(OrderPageLocators.SUBWAY_STATION_BUTTON).click()
        return self.find_element(OrderPageLocators.subway_choice_button(station)).click()

    @allure.step('Ввод номера телефона')
    def input_phone_number(self, phone: str):
        self.enter_text(OrderPageLocators.PHONE_FIELD, phone)

    @allure.step('Ввод даты')
    def input_date(self, date: str):
        self.enter_text(OrderPageLocators.DATE_FIELD, date)
        self.press_enter_button(OrderPageLocators.DATE_FIELD)

    @allure.step('Ввод времени аренды (в сутках)')
    def input_rent_time(self, rent_time: int):
        self.click_element(OrderPageLocators.RENT_TIME_FIELD)
        self.element_is_visible(OrderPageLocators.RENT_TIME_DROPDOWN_MENU)
        self.find_elements(OrderPageLocators.RENTAL_TIME_LIST)[rent_time].click()

    @allure.step('Ввод цвета')
    def input_color(self, color: int):
        self.find_elements(OrderPageLocators.COLOR_CHECKBOXES)[color].click()

    @allure.step('Ввод комментария для курьера')
    def input_comment_for_courier(self, comment: str):
        self.enter_text(OrderPageLocators.COMMENT_FOR_COURIER_FIELD, comment)

    @allure.step('Заполнить данные заказа')
    def fill_user_order_data(self, data_set: dict):
        self.input_name(data_set['name'])
        self.input_surname(data_set['surname'])
        self.input_address(data_set['address'])
        self.input_subway_station(data_set['station'])
        self.input_phone_number(data_set['phone_number'])

    @allure.step('Нажать кнопку "Далее" в процессе оформления заказа')
    def click_next_button(self):
        self.scroll_to_element(OrderPageLocators.NEXT_BUTTON)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить данные об аренде')
    def fill_rent_data(self, data_set: dict):
        self.input_date(data_set['date'])
        self.input_rent_time(data_set['rent_time'])
        for color in data_set['color']:
            self.input_color(color)
        self.input_comment_for_courier(data_set['comment_for_courier'])

    @allure.step('Нажать кнопку "Заказать"')
    def click_final_order_button(self):
        self.click_element(OrderPageLocators.FINAL_ORDER_BUTTON)

    @allure.step('Нажать кнопку "Да" в процессе оформления заказа')
    def click_yes_order_button(self):
        self.click_element(OrderPageLocators.YES_ORDER_BUTTON)

    #@allure.step('Нажать кнопку "Посмотреть статус" после оформления заказа')
    #def click_check_status_button(self):
        #self.click_element(OrderPageLocators.CHECK_STATUS_BUTTON)

    @allure.step('Всплывающее окно с сообщением "Хотите оформить заказ?"')
    def want_to_order_header_visible(self, timeout: int = 10) -> bool:
        return self.element_is_visible(OrderPageLocators.WANT_TO_ORDER_HEADER, timeout)
    
    @allure.step('Всплывающее окно с сообщением "Заказ оформлен "')
    def order_completed_header_visible(self, timeout: int = 10) -> bool:    
        return self.element_is_visible(OrderPageLocators.ORDER_COMPLETED_HEADER, timeout)