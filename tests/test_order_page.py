import allure
import pytest
from ..locators.home_page_locators import HomePageLocators
from ..pages.order_page import OrderPage
from ..data import OrderData
from ..urls import Urls


@allure.epic('Тестирование домашней страницы "Оформление заказа"')
@allure.parent_suite('Оформление заказа')
@allure.suite('Order')
class TestOrderPage:
    @allure.feature('Заказ самоката')
    @allure.story('При нажатии на любую кнопку "Заказать" с домашней страницы открывается форма заказа')
    @allure.title('Заказ самоката до получения номера заказа')
    @allure.description('Проверка корректного оформления заказа с использованием двух наборов данных. Тест '
                        'запускается при нажатии обеих кнопок "Заказать" на домашней странице, с подтвержением'
                        ' всплывающего окна с сообщением об успешном создании заказа')
    @pytest.mark.parametrize('order_button, data_set',
                             [
                                 (HomePageLocators.ORDER_FROM_HOME_HEADER_BUTTON, 'data_set_1'),
                                 (HomePageLocators.ORDER_FROM_HOME_HEADER_BUTTON, 'data_set_2'),
                                 (HomePageLocators.ORDER_FROM_HOME_PAGE_BUTTON, 'data_set_1'),
                                 (HomePageLocators.ORDER_FROM_HOME_PAGE_BUTTON, 'data_set_2'),
                             ])
    def test_create_complete_order_header_and_page_order_buttons_positive(self, driver, order_button, data_set):
        page = OrderPage(driver)
        page.navigate(Urls.HOME_PAGE)
        page.scroll_to_order_button(order_button)
        page.click_order_button(order_button)
        page.fill_user_order_data(OrderData.data_sets[data_set])
        page.click_next_button()
        page.fill_rent_data(OrderData.data_sets[data_set])
        page.click_final_order_button()
        page.click_yes_order_button()
        assert page.order_completed_header_visible()            


    @allure.feature('Заказ самоката')
    @allure.story('При нажатии на любую кнопку "Заказать" с домашней страницы открывается форма заказа')
    @allure.title('Заказ самоката до перехода к заголовку "Про аренду" из header/home')
    @allure.description('Проверка корректного оформления заказа с использованием одного набора данных. Тест '
                        'запускается при нажатии обеих кнопок "Заказать" на домашней странице')
    @pytest.mark.parametrize('order_button',
                             [
                                HomePageLocators.ORDER_FROM_HOME_HEADER_BUTTON,
                                HomePageLocators.ORDER_FROM_HOME_PAGE_BUTTON,
                             ])
    def test_create_order_until_order_complete_positive(self, driver, order_button):
        page = OrderPage(driver)
        page.navigate(Urls.HOME_PAGE)
        page.accept_cookies()
        page.scroll_to_order_button(order_button)
        page.click_order_button(order_button)
        page.fill_user_order_data(OrderData.data_sets['data_set_1'])
        page.click_next_button()
        page.fill_rent_data(OrderData.data_sets['data_set_1'])
        page.click_final_order_button()
        assert page.want_to_order_header_visible()