import allure


from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step ('Переход на страницу восстановить пароль')
    def transition_recover_password(self):
        self.click_to_element(LoginLocators.RECOVER_PASSWORD_BUTTON)
        
    @allure.step('Проверяем, что переход на страницу восстановить пароль выполнен')
    def is_transition_recover_password_successful(self):
        return self.get_text_from_element(LoginLocators.RECOVER_PASSWORD_TEXT)
    
    @allure.step ('Заполняем форму восстановления пароля')
    def fill_recover_form(self):
        self.add_text_to_element(LoginLocators.EMAIL_FIELD, 'petrinho@petr.ru')
        self.click_to_element(LoginLocators.RESTORE_BUTTON)

    @allure.step('Проверяем, что переход после нажатия кнопки Восстановить выполнен')
    def is_transition_reset_successful(self):
        return self.get_text_from_element(LoginLocators.ENTER_CODE_TEXT)
    
    @allure.step ('Показать пароль')
    def show_password(self):
        self.click_to_element(LoginLocators.SHOW_PASSWORD_BUTTON)

    @allure.step('Проверяем, что пароль отображается')
    def is_show_password_successful(self):
        self.wait_element_is_visible(LoginLocators.ACTIVE_FIELD_PASSWORD)
        self.wait_element_is_visible(LoginLocators.SHOW_PASSWORD_TEXT)
    