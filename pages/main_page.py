import allure


from locators.main_locators import MainLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    
    @allure.step('Переход на страницу личный кабинет')
    def transition_personal_account(self):
        self.wait_element_invisible_or_not_present(MainLocators.CLICK_INTERSEPTION)
        self.click_to_element_perform(MainLocators.PERSONAL_ACCOUNT_BUTTON)

    @allure.step('Переход на страницу конструктор')
    def transition_constructor(self):
        self.click_to_element(MainLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Проверяем переход на страницу Конструктор')
    def is_transition_constructor_successful(self):
        return self.get_text_from_element(MainLocators.BURGER_TEXT)
    
    @allure.step('Переход на страницу Лента Заказов')
    def transition_order_feed(self):
        self.click_to_element_js(MainLocators.ORDER_FEED_BUTTON)

    @allure.step('Проверяем переход на страницу Лента Заказов')
    def is_transition_order_feed_successful(self):
        return self.get_text_from_element(MainLocators.ORDER_FEED_TEXT)
    
    @allure.step('Открытие деталей ингредиента')
    def open_detail_ingredient(self):
        self.click_to_element(MainLocators.INGREDIENT_BUTTON)
    
    @allure.step('Проверка открытия деталей ингредиента')
    def is_open_detail_ingredient_succesfull(self):
        return self.get_text_from_element(MainLocators.INGREDIENT_DETAIL_TEXT)

    @allure.step('Закрыть окно детали ингредиента')
    def close_detail_ingredient(self):
        self.click_virt_mouse(MainLocators.CLOSE_DETAIL_BUTTON)

    @allure.step('Проверка закрытия окна детали ингредиента')
    def is_close_detail_ingredient_succesfull(self):
        self.wait_element_invisible_or_not_present(MainLocators.CLOSE_DETAIL_LOCATOR)

    @allure.step('Добавление ингредиента')
    def added_ingredient(self):
        locator_from = MainLocators.KRATOR_BUN_IMG
        locator_to = MainLocators.CONSTRUCTOR_INGREDIENT
        self.drag_and_drop_element(locator_from, locator_to)

    @allure.step('Проверка счетчика')
    def counter_added_ingredient(self):
        return self.get_text_from_element(MainLocators.QUANTITY_COUNER_INGREDIEN)
    
    @allure.step('Оформление заказа')
    def placing_an_order(self):
        self.click_to_element(MainLocators.PLACING_AN_ORDER_BUTTON)

    @allure.step('Проверка отображения заказа')
    def placing_an_order_successful(self):
        return self.wait_element_until_invisibility(MainLocators.DEFAULT_ORDER_TEXT)
    
    @allure.step('Получение номера заказа')
    def get_order(self):
        self.wait_element_until_invisibility(MainLocators.DEFAULT_ORDER_TEXT)
        return self.get_order_number(MainLocators.NUMBER_ORDER_TEXT)
    