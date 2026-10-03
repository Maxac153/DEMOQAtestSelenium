import allure
import pytest

from src.api.demoq.request.api.client import DemoQaClient


@allure.parent_suite("API-тесты")
@allure.suite("Account API")
@allure.feature("Управление пользователями")
class TestAccountApi:
    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.account
    @allure.story("Получение данных пользователя")
    @allure.title("Получение информации о пользователе по ID")
    def test_get_user(self, client: DemoQaClient, created_user, token):
        with allure.step("Получение данных пользователя"):
            response = client.get_user(
                user_id=created_user["user_id"],
                token=token,
            )

        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 200, (
                f"Ожидался статус-код 200, "
                f"получен {response.status_code}. "
                f"Тело ответа: {response.body}"
            )

        with allure.step("Проверка совпадения userId"):
            assert response.body["userId"] == created_user["user_id"], (
                f"Ожидался userId {created_user['user_id']}, "
                f"получен {response.body.get('userId')}. "
                f"Тело ответа: {response.body}"
            )

        with allure.step("Проверка совпадения username"):
            assert response.body["username"] == created_user["user_name"], (
                f"Ожидался username {created_user['user_name']}, "
                f"получен {response.body.get('username')}. "
                f"Тело ответа: {response.body}"
            )
