from selenium.webdriver.common.by import By


class LoginLocators:
    # локаторы переходов
    RECOVER_PASSWORD_BUTTON = By.XPATH, "//a[text()='Восстановить пароль']" # кнпока восстановить пароль
    RESTORE_BUTTON = By.XPATH, "//button[text()='Восстановить']" # кнопка Восстановить
    SHOW_PASSWORD_BUTTON = By.XPATH, "//div[@class='input__icon input__icon-action']" # кнопка показать/скрыть пароль

    EMAIL_FIELD = By. XPATH, "//input[@type='text']" # поле email в восстановлении пароля
    ACTIVE_FIELD_PASSWORD = By.XPATH, "//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']" # поле пароль стало активно

    INFORMATION_TEXT = By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']" # подсказка из личного кабинета
    RECOVER_PASSWORD_TEXT = By.XPATH, "//h2[text()='Восстановление пароля']" # текст Восстановаление пароля
    ENTER_CODE_TEXT = By.XPATH, "//label[text()='Введите код из письма']" # текст Введите код из письма
    SHOW_PASSWORD_TEXT = By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='text']" # проверка отображения значения пароля