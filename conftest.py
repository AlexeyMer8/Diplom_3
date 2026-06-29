import pytest
import requests
import random
import string
import allure


from urls import BASE_URL, CREATE_USER_URL, LOGIN_URL
from selenium import webdriver
from pages.login_page import LoginPage
from pages.personal_account_page import PersonalAccountPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome()
    else:
        browser = webdriver.Firefox()

    browser.set_window_size(1920, 1080)

    yield browser
    browser.quit()

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    return page

@pytest.fixture
def personal_account_page(driver):
    page = PersonalAccountPage(driver)
    return page

@pytest.fixture
def main_page_login(driver):
    page = MainPage(driver)
    page.go_to_url(LOGIN_URL)
    return page

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(BASE_URL)
    return page

@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    return page

@pytest.fixture
def login_user(driver):
    """Логинит пользователя через UI и возвращает main_page"""
    main_page = MainPage(driver)
    main_page.transition_personal_account()
    
    personal_account_page = PersonalAccountPage(driver)
    personal_account_page.fill_authorization_form(
        email='petrinho@petr.ru',
        password='555555'
    )
    
    # Возвращаем main_page для дальнейших действий
    return main_page

@pytest.fixture
def create_user():
    """
    Фикстура для создания пользователя через API.
    Возвращает объект с данными пользователя.
    
    Использование:
        user = create_user()
        print(user.email, user.password, user.name)
    """
    class UserData:
        """Класс для хранения данных пользователя"""
        def __init__(self, email, password, name, api_response=None, status_code=None):
            self.email = email
            self.password = password
            self.name = name
            self.api_response = api_response
            self.status_code = status_code
        
        def __repr__(self):
            return f"UserData(email='{self.email}', password='{self.password}', name='{self.name}')"
    
    def _generate_random_string(length):
        """Генерация случайной строки"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    def _create_user():
        """Создание пользователя через API"""
        # Генерируем данные
        email = f"{_generate_random_string(10)}@yandex.ru"
        password = _generate_random_string(10)
        name = _generate_random_string(10)
        
        # Отправляем запрос
        params = {"email": email, "password": password, "name": name}
        response = requests.post(f'{CREATE_USER_URL}', data=params)
        
        # Проверяем ответ
        if response.status_code == 200:
            user_data = response.json()
            
            # Логируем в отчет
            allure.attach(
                f"Email: {email}\nPassword: {password}\nName: {name}",
                name="Созданный пользователь",
                attachment_type=allure.attachment_type.TEXT
            )
            
            # Возвращаем объект с данными
            return UserData(
                email=email,
                password=password,
                name=name,
                api_response=user_data,
                status_code=response.status_code
            )
        else:
            raise Exception(f"Failed to create user: {response.text}")
    return _create_user
    
    

