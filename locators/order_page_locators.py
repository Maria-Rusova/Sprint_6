from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Заголовок страницы заказа
    ORDER_HEADER = (By.XPATH, ".//div[text()='Для кого самокат']")

    # Данные заказа
    NAME_FIELD = (By.XPATH, ".//input[contains(@placeholder, '* Имя')]")
    SURNAME_FIELD = (By.XPATH, ".//input[contains(@placeholder, '* Фамилия')]")
    ADDRESS_FIELD = (By.XPATH, ".//input[contains(@placeholder, '* Адрес: куда привезти заказ')]")
    SUBWAY_STATION_BUTTON = (By.XPATH, ".//input[contains(@placeholder, '* Станция метро')]")
    PHONE_FIELD = (By.XPATH, ".//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]")

    # Геттер станции метро
    @staticmethod
    def subway_choice_button(station: str):
        return (By.XPATH, f".//div[text()='{station}']/parent::button")

    # Кнопка "Далее" страницы заказа
    NEXT_BUTTON = (By.XPATH, ".//div[@class='Order_NextButton__1_rCA']/button")

    # Заголовок "Про аренду" в ходе заказа
    ABOUT_RENT_HEADER = (By.XPATH, ".//div[text()='Про аренду']")

    # Данные об аренде
    DATE_FIELD = (By.XPATH, ".//input[contains(@placeholder, '* Когда привезти самокат')]")
    RENT_TIME_FIELD = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    RENT_TIME_DROPDOWN_MENU = (By.XPATH, ".//div[@class='Dropdown-menu']")
    RENTAL_TIME_LIST = (By.XPATH, ".//div[@class='Dropdown-option']")
    SCOOTER_COLOR_FIELD = (By.XPATH, ".//input[contains(@placeholder, '* Цвет самоката')]")
    COLOR_CHECKBOXES = (By.XPATH, ".//div[contains(text(), 'Цвет')]/parent::div//input")
    COMMENT_FOR_COURIER_FIELD = (By.XPATH, ".//input[contains(@placeholder, 'Комментарий для курьера')]")

    # Всплывающее окно
    WANT_TO_ORDER_HEADER = (By.CSS_SELECTOR, "div.Order_Modal__YZ-d3")

    # Кнопки "Да"
    YES_ORDER_BUTTON = (By.XPATH, ".//button[text()='Да']")

    # Кнопки "Назад" и "Заказать" на странице заказа
    GO_BACK_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Назад']")
    FINAL_ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']")

    # Заголовок после оформления заказа "Заказ оформлен"
    ORDER_COMPLETED_HEADER = (By.CSS_SELECTOR, "div.Order_ModalHeader__3FDaJ")

    # Локатор строки с номером заказа
    ORDER_NUM_STR = (By.XPATH, "//div[contains(text(), 'Номер заказа')]")

    # Кнопка "Посмотреть статус"
    CHECK_STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")

    # Текстовое поле с номером заказа
    ORDER_NUM_TRACK_FIELD = (By.CSS_SELECTOR, "div.Order_Text__2broi")