import allure
import pytest

from src.api.demoq.request.api.client import DemoQaClient


@allure.parent_suite("API-тесты")
@allure.suite("Account API")
@allure.feature("Аккаунт")
class TestAccountApi:
    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.account
    @allure.story("Авторизация пользователя")
    @allure.title("Проверка успешной авторизации пользователя")
    def test_authorized(
            self,
            client: DemoQaClient,
            created_user: dict[str, str]
    ):
        with allure.step("Авторизация пользователя"):
            response = client.authorized(
                user_name=created_user["user_name"],
                password=created_user["password"],
            )

        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 200, (
                f"Ожидался статус-код 200, получен {response.status_code}. "
                f"Тело ответа: {response.body}"
            )

        with allure.step("Проверка результата авторизации"):
            assert response.body is True, (
                f"Ожидался результат авторизации True, "
                f"получен: {response.body}"
            )
