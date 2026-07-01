import allure


class TestsTransitionPage:
    
    @allure.title('Войти в аккаунт')
    def test_transition_personal_account_page(self, personal_account_page, main_page_login):
        personal_account_page.fill_authorization_form()
        main_page_login.transition_personal_account()
        
        assert personal_account_page.is_transition_personal_account_successful() == 'Профиль'

    @allure.title('Перехода в раздел История заказов')
    def test_transition_orer_feed(self, personal_account_page, main_page_login):
        personal_account_page.fill_authorization_form()
        main_page_login.transition_personal_account()
        personal_account_page.transition_history_order()

        assert personal_account_page.is_transition_history_order_successful() == 'История заказов'

    @allure.title('Выход из аккаунта')
    def test_exit_personal_account_page(self, personal_account_page, main_page_login):
        personal_account_page.fill_authorization_form()
        main_page_login.transition_personal_account()
        personal_account_page.exit_personal_account()

        assert personal_account_page.is_exit_personal_account_successful() == 'Вход'

