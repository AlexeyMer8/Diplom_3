from selenium.webdriver.common.by import By


class PersonalAccountLocators:
    # локаторы кнопок
    EXIT_BUTTON = By.XPATH, "//button[text()='Выход']" # кнопка Выход
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти']" # кнопка Войти
    PROFILE_BUTTON = By.XPATH, "//a[text()='Профиль']" # кнпока Профиль
    HISTORY_ORDER_BUTTON = By.XPATH, "//a[text()='История заказов']" # кнопка История заказов
    ACTIVE_HISTORY_ORDER_BUTTON = By.XPATH, "//a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive Account_link_active__2opc9' and text()='История заказов']" # кнопка История заказов активна

    # локаторы полей
    EMAIL_FIELD = By.XPATH, "//input[@name='name']" # поле email
    PASSWORD_FIELD = By.XPATH, "//input[@name='Пароль']" # поле пароль
    ENTER_TEXT = By.XPATH, "//h2[text()='Вход']" # текст Вход
    

