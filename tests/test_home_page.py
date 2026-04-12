import allure
import pytest
from ..urls import Urls
from ..questions_data import Questions
from ..pages.home_page import HomePage
from ..locators.home_page_locators import HomePageLocators


@allure.epic('Тестирование домашней страницы "Яндекс Самокат"')
@allure.parent_suite('Домашняя страница')
@allure.suite('Home')
class TestHomePage:
    # Вопросы о важном, отдельный тест на каждый вопрос
    @allure.feature('Нажатие на кнопки "Вопросы о важном"')
    @allure.story('При нажатии на вопрос в разделе "Вопросы о важном" выпадает текст с ответом')
    @allure.title('Выпадение ответа при нажатии')
    @allure.description('Проверка нажатия всех 8-ми кнопок с вопросами и получение требуемых ответов')
    @pytest.mark.parametrize(
        "question_id, expected_reply",
        [
            (0, Questions.answers[1]),
            (1, Questions.answers[2]),
            (2, Questions.answers[3]),
            (3, Questions.answers[4]),
            (4, Questions.answers[5]),
            (5, Questions.answers[6]),
            (6, Questions.answers[7]),
            (7, Questions.answers[8]),
        ],
        ids=[
            "Q1: how to order?",
            "Q2: delivery time",
            "Q3: payment methods",
            "Q4: cancel order",
            "Q5: return policy",
            "Q6: warranty",
            "Q7: support contacts",
            "Q8: discounts"
        ]
    )
    def test_click_on_all_questions_important(self, driver, question_id, expected_reply):
        page = HomePage(driver)
        page.navigate(Urls.HOME_PAGE)
        page.scroll_to_question_about_important_section()
        page.click_question_buttons(question_id)

        assert page.element_is_visible(HomePageLocators.get_question_id_text(question_id)) \
               and page.get_question_button_text(question_id).text == expected_reply

    # вход в сценарий: кнопки «Заказать» вверху страницы и внизу
    @allure.feature('Переход на страницу Заказа с домашней страницы')
    @allure.story('При нажатии на кнопку "Заказать" осуществляется переход на страницу заказа')
    @allure.title('Переход на страницу "Оформление заказа" из header/home')
    @allure.description('Проверка коррекнтного перехода на страницу "Оформление заказа" по кнопке "Заказать" из header/home '
                        'домашней страницы и блока "Как это работает"')
    @pytest.mark.parametrize('order_button',
                             [
                                 HomePageLocators.ORDER_FROM_HOME_HEADER_BUTTON,
                                 HomePageLocators.ORDER_FROM_HOME_PAGE_BUTTON
                             ]
                             )
    def test_click_on_order_buttons_from_header_and_home_sections(self, driver, order_button): 
        page = HomePage(driver)
        page.navigate(Urls.HOME_PAGE)
        page.scroll_to_order_button(order_button)
        page.click_order_button(order_button)
        page.wait_for_order_header_text()
        assert page.current_url() == Urls.ORDER_PAGE

    # с домашней через логотип Яндекса, ведет на галвную Дзена
    @allure.feature('Нажатие на лого "Яндекс" с домашней страницы')
    @allure.story('При нажатии на лого "Яндекс" открывается новая вкладка dzen')
    @allure.title('Открытие вкладки /order в шапке главной страницы')
    @allure.description('Проверка корректных открытия и перехода на страницу dzen.ru после клика на логотип "Яндекс" в '
                        'шапке главной страницы')
    def test_click_on_yandex_logo_from_home_page(self, driver):
        page = HomePage(driver)
        page.navigate(Urls.HOME_PAGE)
        page.click_yandex_logo_button()
        page.switch_to(1)
        page.wait_for_url()
        assert Urls.DZEN_HOME_PAGE in page.current_url()

    # cо страници заказа через логотип Яндекса, ведет на галвную Дзена
    @allure.feature('Нажатие на лого "Яндекс" со страницы "Оформление заказа"')
    @allure.story('При нажатии на лого "Яндекс" открывается новая вкладка dzen.ru')
    @allure.title('Открытие вкладки /order в шапке страницы "Оформление заказа"')
    @allure.description('Проверка корректных открытия и перехода на страницу dzen.ru после клика на логотип "Яндекс" в '
                        'шапке страницы "Оформление заказа"')
    def test_click_on_yandex_logo_from_order_page(self, driver):
        page = HomePage(driver)
        page.navigate(Urls.ORDER_PAGE)
        page.click_yandex_logo_button()
        page.switch_to(1)
        page.wait_for_url()
        assert Urls.DZEN_HOME_PAGE in page.current_url()

    # клик по логотипу «Самокат» на главной странице не приводит к изменению URL
    @allure.feature('Нажатие на лого "Самокат" с домашней страницы"')
    @allure.story('При нажатии на лого "Самокат" URL дрес не меняется')
    @allure.title('Остаемся на домашней странице')
    @allure.description('Проверка корректных открытия и перехода на домашнюю страницу после клика на логотип Самокат в '
                        'шапке домашней страницы')
    def test_click_on_scooter_logo_from_home_page(self, driver):
        page = HomePage(driver)
        page.navigate(Urls.HOME_PAGE)
        page.click_scooter_logo_button()
        assert Urls.HOME_PAGE == page.current_url()

    # клик по логотипу «Самокат» на странице заказа выполняет переход на главную страницу
    @allure.feature('Нажатие на лого "Самокат" со страницы "Оформление заказа"')
    @allure.story('При нажатии на лого "Самокат" открывается домашняя страница')
    @allure.title('Открытие домашней страницы')
    @allure.description('Проверка корректных открытия и перехода на страницу dzen.ru после клика на логотип "Самокат" в'
                        'шапке страницы "Оформление заказа"')
    def test_click_on_scooter_logo_from_order_page(self, driver):
        page = HomePage(driver)
        page.navigate(Urls.ORDER_PAGE)
        page.click_scooter_logo_button()
        assert Urls.HOME_PAGE == page.current_url()