import allure
import pytest

from src.api.demoq.request.api.client import DemoQaClient


@allure.parent_suite("API-test")
@allure.suite("DemoQA")
@allure.feature("Пользователь")
class TestUserApi:
    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.positive
    @allure.story("Создание и авторизация пользователя")
    @allure.title("Создание пользователя и получение токена")
    def test_create_user_and_get_token(
            self,
            client: DemoQaClient,
            created_user: dict[str, str],
            token: str,
    ):
        with allure.step("Проверка данных созданного пользователя"):
            assert created_user["user_id"], "user_id отсутствует"
            assert created_user["user_name"].startswith("api_user_"), "Некорректный user_name"
            assert created_user["password"], "password отсутствует"

        with allure.step("Проверка токена"):
            assert token, "Токен отсутствует"
            assert isinstance(token, str), "Токен должен быть строкой"
