import allure


from locators.order_locators import OrderLocators
from pages.base_page import BasePage

    
class OrderPage(BasePage):
    
    @allure.step('Выход из заказа')
    def close_order(self):
        self.click_to_element_js(OrderLocators.CLOSE_PLACING_ORDER_BUTTON)

    @allure.step('Открыть данные о заказе')
    def get_info_order(self, number_order):
        locator_number_order = self.format_locators(OrderLocators.NUMBER_ORDER_IN_LIST_TEXT, NUMBER_ORDER=number_order)
        element = self.wait_elements_is_visible(locator_number_order)
        self.click_to_element(locator_number_order)
        element = self.wait_element_is_visible(locator_number_order)
        return element is not None
    
    @allure.step('Заказ добавлен в список готовых')
    def order_successful(self, number_order):
        locator_number_order = self.format_locators(OrderLocators.COUNTER_IN_WORK_ORDER, NUMBER_ORDER=number_order)
        self.wait_element_invisible_or_not_present(OrderLocators.ORDERS_COMPLETED_TEXT)
        element = self.wait_element_is_visible(locator_number_order)
        return element is not None
    
    @allure.step('Получить количество заказов')
    def get_counter_time(self, locator):
        return self.get_text_from_element(locator)
    
    @allure.step('Получить id последнего заказа')
    def get_id_last_order(self):
        return self.get_text_from_element(OrderLocators.LAST_ELEMENT)
    
    @allure.step('Проверяем, что заказ из истории заказов отображается в ленте')
    def show_id_order_with_order_feed(self, id):
        locator_number_order = self.format_locators(OrderLocators.NUMBER_ORDER_IN_LIST_TEXT, NUMBER_ORDER=id)
        element = self.wait_elements_is_visible(locator_number_order)
        return element is not None
