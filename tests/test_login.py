import allure


class TestsLoginPage:
    
    @allure.title('Переход на страницу восстановить пароль')
    def test_transition_recover_password_page(self, login_page, main_page_login):
        main_page_login.transition_personal_account()
        login_page.transition_recover_password()
        
        assert login_page.is_transition_recover_password_successful() == 'Восстановление пароля'

    @allure.title('Переход на страницу подтверждения восстановления пароля')
    def test_transition_reset_page(self, login_page, main_page_login):
        main_page_login.transition_personal_account()
        login_page.transition_recover_password()
        login_page.fill_recover_form()
        
        assert login_page.is_transition_reset_successful() == 'Введите код из письма'

    @allure.title('Показать пароль')
    def test_show_password(self, login_page, main_page_login):
        main_page_login.transition_personal_account()
        login_page.transition_recover_password()
        login_page.fill_recover_form()
        login_page.show_password()
        
        assert login_page.is_transition_reset_successful() == 'Введите код из письма'