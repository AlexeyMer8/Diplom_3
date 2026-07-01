import allure


class TestsMainPage:
    
    # @allure.title('Переход на страницу Конструктор')
    # def test_transition_constructor_page(self, main_page):
    #     main_page.transition_order_feed()
    #     main_page.transition_constructor()
        
    #     assert main_page.is_transition_constructor_successful() == 'Соберите бургер'

    # @allure.title('Переход на страницу Лента Заказов')
    # def test_transition_order_feed_page(self, main_page):
    #     main_page.transition_order_feed()
        
    #     assert main_page.is_transition_order_feed_successful() == 'Лента заказов'

    # @allure.title('Открытие деталей ингредиентов')
    # def test_open_detail_ingredient(self, main_page):
    #     main_page.open_detail_ingredient()
        
    #     assert main_page.is_open_detail_ingredient_succesfull() == 'Детали ингредиента'

    # @allure.title('Закрытие окна детали ингредиента')
    # def test_close_detail_ingredient(self, main_page):
    #     main_page.open_detail_ingredient()
    #     main_page.close_detail_ingredient()
        
    #     assert main_page.is_close_detail_ingredient_succesfull() == None

    # @allure.title('Добавление игредиента')
    # def test_added_ingredient(self, main_page):
    #     main_page.added_ingredient()
        
    #     assert main_page.counter_added_ingredient() == '2'

    @allure.title('Оформление заказа')
    def test_placing_an_order(self, main_page, personal_account_page, create_user):
        user = create_user()
        main_page.transition_personal_account()
        personal_account_page.fill_authorization_form_api(
            email=user.email,
            password=user.password
        )
        main_page.added_ingredient()
        main_page.placing_an_order()

        assert main_page.placing_an_order_successful() == True

        