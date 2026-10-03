import allure
import pytest

from src.api.demoq.request.api.client import DemoQaClient


@allure.parent_suite("API-тесты")
@allure.suite("Account API")
@allure.feature("Аккаунт")
class TestAccountApi:
    @pytest.mark.api
    @pytest.mark.negative
    @pytest.mark.account
    @allure.story("Авторизация с некорректными данными")
    @allure.title("Отклонение авторизации с неверным паролем")
    def test_authorized_with_invalid_password(
            self,
            client: DemoQaClient,
            created_user: dict[str, str],
    ):
        with allure.step("Авторизация с неверным паролем"):
            response = client.authorized(
                user_name=created_user["user_name"],
                password="WrongPassword123!",
            )

        with allure.step("Проверка отказа в авторизации"):
            assert response.status_code == 404, (
                f"Ожидался статус-код 404, "
                f"получен {response.status_code}. "
                f"Тело ответа: {response.body}"
            )

        with allure.step("Проверка сообщения об ошибке"):
            assert response.body == {
                "code": "1207",
                "message": "User not found!",
            }, (
                f"Ожидалось сообщение об ошибке о ненайденном пользователе, "
                f"получен ответ: {response.body}"
            )
