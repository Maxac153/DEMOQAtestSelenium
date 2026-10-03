import allure
import pytest

from src.api.demoq.request.api.client import DemoQaClient


@allure.parent_suite("API-тесты")
@allure.suite("BookStore API")
@allure.feature("Коллекция книг")
class TestBookStoreCollectionApi:
    @pytest.mark.api
    @pytest.mark.smoke
    @pytest.mark.positive
    @pytest.mark.book_store
    @allure.story("Добавление книги в коллекцию")
    @allure.title("Добавление книги в коллекцию пользователя")
    def test_add_book_to_collection(
            self, client: DemoQaClient, created_user, token
    ):
        with allure.step("Получение списка книг"):
            books_response = client.get_books()

        with allure.step("Проверка статус-кода получения книг"):
            assert books_response.status_code == 200, (
                f"Ожидался статус-код 200, "
                f"получен {books_response.status_code}. "
                f"Тело ответа: {books_response.body}"
            )

        with allure.step("Проверка наличия книг в ответе"):
            assert books_response.body.get("books"), (
                f"Список книг пуст или отсутствует: {books_response.body}"
            )

        with allure.step("Извлечение ISBN первой книги"):
            isbn = books_response.body["books"][0]["isbn"]

        with allure.step("Добавление книги в коллекцию пользователя"):
            response = client.add_book(
                user_id=created_user["user_id"],
                token=token,
                isbn=isbn,
            )

        with allure.step("Проверка статус-кода добавления книги"):
            assert response.status_code in (200, 201), (
                f"Ожидался статус-код 200 или 201, "
                f"получен {response.status_code}. "
                f"Тело ответа: {response.body}"
            )
