import allure
import pytest

from src.api.demoq.request.api.client import DemoQaClient


@allure.parent_suite("API-тесты")
@allure.suite("BookStore API")
@allure.feature("Книжный магазин")
class TestBookStoreApi:
    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.book_store
    @allure.story("Получение списка книг")
    @allure.title("Получение всех книг из книжного магазина")
    def test_get_books(self, client: DemoQaClient):
        with allure.step("Получение списка книг"):
            response = client.get_books()

        with allure.step("Проверка статус-кода ответа"):
            assert response.status_code == 200, (
                f"Ожидался статус-код 200, "
                f"получен {response.status_code}. "
                f"Тело ответа: {response.body}"
            )

        with allure.step("Проверка наличия списка книг в ответе"):
            assert "books" in response.body, (
                f"В ответе отсутствует поле 'books': {response.body}"
            )

        with allure.step("Проверка типа списка книг"):
            assert isinstance(response.body["books"], list), (
                "Поле 'books' должно содержать список"
            )

        with allure.step("Проверка наличия книг"):
            assert response.body["books"], (
                "Список книг не должен быть пустым"
            )
