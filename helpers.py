import requests
import random
import string
import allure

from urls import CREATE_USER_URL


class UserData:
    def __init__(self, email, password, name, api_response=None, status_code=None):
        self.email = email
        self.password = password
        self.name = name
        self.api_response = api_response
        self.status_code = status_code
    
    def __repr__(self):
        return f"UserData(email='{self.email}', password='{self.password}', name='{self.name}')"


class UserHelper:

    def __init__(self):
        self.url = f'{CREATE_USER_URL}'
    
    @staticmethod
    def generate_random_string(length):
        """Генерация случайной строки"""
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
    
    def create_user(self, params=None):
        """Создание пользователя через API"""
        if params is None:
            params = self.generate_user_data()
        
        response = requests.post(self.url, data=params)

        if response.status_code == 200:
            user_data = response.json()
            
            # Возвращаем объект с данными
            return UserData(
                email=params['email'],
                password=params['password'],
                name=params['name'],
                api_response=user_data,
                status_code=response.status_code
            )
        else:
            raise Exception(f"Failed to create user: {response.text}")
    
    def generate_user_data(self):
        """Генерация случайных данных пользователя"""
        email = f"{self.generate_random_string(10)}@yandex.ru"
        password = self.generate_random_string(10)
        name = self.generate_random_string(10)
        
        return {
            "email": email,
            "password": password,
            "name": name
        }


# Упрощенная функция для создания пользователя
def create_test_user():
    """Создание тестового пользователя через API"""
    helper = UserHelper()
    return helper.create_user()