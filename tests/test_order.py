import allure
import pytest


from locators.order_locators import OrderLocators


class TestsMainPage:

    @allure.title('Открыть окно с деталями заказа')
    def test_transition_order_feed_page(self, main_page_login, order_page, personal_account_page):
        personal_account_page.fill_authorization_form()
        main_page_login.added_ingredient()
        main_page_login.placing_an_order()
        number_order_with_symbol = f'#0{main_page_login.get_order()}'
        order_page.close_order()
        main_page_login.transition_order_feed()
        
        assert order_page.get_info_order(number_order_with_symbol) == True 
        
    @allure.title('Заказ добавлен в список в работе')
    def test_order_successful(self, main_page_login, order_page, personal_account_page):
        personal_account_page.fill_authorization_form()
        main_page_login.added_ingredient()
        main_page_login.placing_an_order()
        number_order = main_page_login.get_order()
        order_page.close_order()
        main_page_login.transition_order_feed()
        
        assert order_page.order_successful(number_order) == True


    @pytest.mark.parametrize('locator', [
        (
            (OrderLocators.COMPLETED_ALL_TIME_TEXT)
        ),
        (
            (OrderLocators.COMPLETED_TODAY_TEXT)
        ),
    ])
    @allure.title('Увеличился счетчик выполнено за все время')
    def test_counter_all_time_increased(self, main_page, order_page, personal_account_page, locator):
        main_page.transition_order_feed()
        counter_order_all = order_page.get_counter_time(locator)
        print(counter_order_all)
        main_page.transition_constructor()
        main_page.transition_personal_account()
        personal_account_page.fill_authorization_form()
        main_page.added_ingredient()
        main_page.placing_an_order()
        order_page.close_order()
        main_page.transition_order_feed()
        counter_order_all_new = order_page.get_counter_time(locator)
        
        assert counter_order_all < counter_order_all_new

    @allure.title('Проверка id из статуса заказа')
    def test_validation_history_order_successful(self, main_page, order_page, personal_account_page, main_page_login):
        personal_account_page.fill_authorization_form()
        main_page_login.transition_personal_account()
        personal_account_page.transition_history_order()
        id = order_page.get_id_last_order()
        print(id)
        main_page.transition_order_feed()
        
        assert order_page.show_id_order_with_order_feed(id) == True
        