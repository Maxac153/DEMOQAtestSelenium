import allure
import pytest


@allure.parent_suite("API-test")
@allure.suite("Account API")
@allure.feature("Аккаунт")
class TestAccountApi:
    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.account
    @allure.story("Генерация токена")
    @allure.title("Проверка генерации токена")
    def test_generate_token(self, token: str):
        with allure.step("Проверка наличия токена"):
            assert token, "Токен отсутствует"

        with allure.step("Проверка типа токена"):
            assert isinstance(token, str), "Токен должен быть строкой"
