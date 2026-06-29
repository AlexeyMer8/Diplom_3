from selenium.webdriver.common.by import By


class MainLocators:
    # локаторы переходов
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']" # кнопка личный кабинет
    ORDER_FEED_BUTTON = By.XPATH, "//p[text()='Лента Заказов']" # кнопка лента заказов
    FORGOT_PASSWORD_BUTTON = By.XPATH, "//a[text()='Восстановить пароль']" # кнпока восстановить пароль
    CONSTRUCTOR_BUTTON = By.XPATH, "//p[text()='Конструктор']" # кнопка конструктор
    INGREDIENT_BUTTON = By.XPATH, "//p[text()='Краторная булка N-200i']" # выбор ингредиента
    DETAIL_INGREDIENT_BUTTON = By.XPATH, "//h2[text()='Детали ингредиента']" # детали ингредиента
    CLOSE_DETAIL_BUTTON = By.XPATH, "//h2[text()='Детали ингредиента']/parent::div/parent::div/button" # кнопка закрыть окно Детали ингредиента
    PLACING_AN_ORDER_BUTTON = By.XPATH, "//button[text()='Оформить заказ']" # кнопка оформить заказ
    KRATOR_BUN_IMG = By.XPATH, "//img[@alt='Краторная булка N-200i']" # краторная булка
    
    NUMBER_ORDER_TEXT= By.XPATH, "//div/h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']" # номер заказа
    INFORMATION_TEXT = By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']" # подсказка из личного кабинета
    BURGER_TEXT = By.XPATH, "//h1[text()='Соберите бургер']" # текст Соберите бургер
    ORDER_FEED_TEXT = By.XPATH, "//div/h1[text()='Лента заказов']" # текст Лента заказов
    INGREDIENT_DETAIL_TEXT = By.XPATH, "//h2[text()='Детали ингредиента']" # текст Детали ингредиентов
    CLOSE_DETAIL_LOCATOR = By.XPATH, "//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']" # проверка закрытия модального окна ингредиента
    QUANTITY_COUNER_INGREDIEN = By.XPATH, "//img[@alt='Краторная булка N-200i']/parent::a//p[@class='counter_counter__num__3nue1']" # счетчик ингредиента
    CONSTRUCTOR_INGREDIENT = By.XPATH, "//span[text()='Перетяните булочку сюда (верх)']" # сбор ингредиентов
    DEFAULT_ORDER_TEXT = By.XPATH, "//h2[text()='9999']" # локатор дефолтного заказа
    CLICK_INTERSEPTION = By.XPATH, "//div[@class = 'Modal_modal_overlay__x2ZCr']" 

