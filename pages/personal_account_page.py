import allure
import data


from locators.personal_account_locators import PersonalAccountLocators
from pages.base_page import BasePage

    
class PersonalAccountPage(BasePage):
    
    @allure.step('Заполняем форму авторизации')
    def fill_authorization_form(self):
        self.add_text_to_element(PersonalAccountLocators.EMAIL_FIELD, data.email)
        self.add_text_to_element(PersonalAccountLocators.PASSWORD_FIELD, data.password)
        self.click_to_element(PersonalAccountLocators.LOGIN_BUTTON)
    
    @allure.step('Заполняем форму авторизации из сгенерированного пользователя')
    def fill_authorization_form_api(self, email, password):
        self.add_text_to_element(PersonalAccountLocators.EMAIL_FIELD, email)
        self.add_text_to_element(PersonalAccountLocators.PASSWORD_FIELD, password)
        self.click_to_element(PersonalAccountLocators.LOGIN_BUTTON)

    @allure.step('Выйти из профиля')
    def exit_personal_account(self):
        self.click_to_element(PersonalAccountLocators.EXIT_BUTTON)

    @allure.step('Проверяем, что переход в личный кабинет выполнен')
    def is_transition_personal_account_successful(self):
        return self.get_text_from_element(PersonalAccountLocators.PROFILE_BUTTON)
    
    @allure.step('Проверяем, что выход из личного кабинета выполнен')
    def is_exit_personal_account_successful(self):
        return self.get_text_from_element(PersonalAccountLocators.ENTER_TEXT)

    @allure.step('Переход в историю заказов')
    def transition_history_order(self):
        self.click_virt_mouse(PersonalAccountLocators.HISTORY_ORDER_BUTTON)

    @allure.step('Проверяем, что переход в личный кабинет выполнен')
    def is_transition_history_order_successful(self):
        return self.get_text_from_element(PersonalAccountLocators.ACTIVE_HISTORY_ORDER_BUTTON)
