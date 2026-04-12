from selenium.webdriver.common.by import By


class HomePageLocators:
    
    QUESTIONS_ABOUT_IMPORTANT_TITLE = (By.XPATH, ".//div[text()='Вопросы о важном']")  # Заголовок "Вопросы о важном"
    QUESTION_BUTTONS = (By.XPATH, ".//div[@class='accordion__button']")  # Список кнопок "Вопросы о важном"
    
    @staticmethod
    def get_question_button(reply) -> tuple[str, str]:
       return (By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{reply}']/p") # Геnтер пунктов "Вопросы о важном"
    
    @staticmethod
    def get_question_id_text(question_id) -> tuple[str, str]:
        return (By.XPATH, f".//div[@id='accordion__panel-{question_id}' and not(@hidden)]") # Геттер пунктов "Вопросы о важном" id


    ORDER_FROM_HOME_HEADER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header')]/button[text()='Заказать']")  # Кнопка "Заказать" на главной странице
    ORDER_FROM_HOME_PAGE_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home')]/button[text()='Заказать']")  # Кнопка "Заказать" в низу страницы
    YANDEX_LOGO = (By.XPATH, ".//img[@alt='Yandex']/parent::a[contains(@href, 'yandex')]")  # "Яндекс" — хейдер лого "ЯндексСамокат"
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'LogoScooter')]")  # "Самокат" — хейдер лого "ЯндексСамокат"

    ACCEPT_COOKIES_BUTTON = (By.XPATH, ".//button[@id='rcc-confirm-button']")  # Кнопка "Да все привыкли" 