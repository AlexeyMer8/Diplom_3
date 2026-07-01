import pytest
import helpers


from urls import BASE_URL, LOGIN_URL
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
    return helpers.create_test_user
