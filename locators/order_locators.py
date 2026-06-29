from selenium.webdriver.common.by import By

class OrderLocators:
    ORDER_FEED_TEXT = By.XPATH, "//h1[text()='Лента заказов']" # текст Лента заказов

    CLOSE_PLACING_ORDER_BUTTON = By.XPATH, "//p[text()='идентификатор заказа']/parent::div/parent::div/button" # закрыть номер заказа
    NUMBER_ORDER_IN_LIST_TEXT = By.XPATH, "//p[text()='{NUMBER_ORDER}']"
    HISTORY_ORDERS_TEXT = By.XPATH, "//p[@class='text text_type_digits-default']" # локатор списка заказов
    COUNTER_IN_WORK_ORDER = By.XPATH, "//p[text()='В работе:']/parent::div/ul/li[text()='{NUMBER_ORDER}']" # поис id заказа среди значений в работе
    ORDERS_COMPLETED_TEXT = By.XPATH, "//li[text()='Все текущие заказы готовы!']" # все заказы готовы
    COMPLETED_ALL_TIME_TEXT = By.XPATH, "//p[text()='Выполнено за все время:']/parent::div/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    COMPLETED_TODAY_TEXT = By.XPATH, "//p[text()='Выполнено за сегодня:']/parent::div/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']"
    LAST_ELEMENT = By.XPATH, "(//li//p[@class= 'text text_type_digits-default'])[last()]"