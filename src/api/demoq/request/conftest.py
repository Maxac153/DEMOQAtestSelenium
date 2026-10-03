import uuid

import allure
import pytest
from faker import Faker

from src.api.demoq.request.api.client import DemoQaClient

fake = Faker()


@pytest.fixture(scope="session")
def client() -> DemoQaClient:
    return DemoQaClient()


@pytest.fixture(scope="session")
def user_data() -> dict[str, str]:
    return {
        "user_name": f"api_user_{uuid.uuid4().hex[:10]}",
        "password": "Qwerty123!",
    }


@pytest.fixture(scope="session")
def created_user(client: DemoQaClient, user_data: dict[str, str]):
    with allure.step("Create test user"):
        response = client.create_user(
            user_name=user_data["user_name"],
            password=user_data["password"],
        )

    assert response.status_code == 201, response.body

    return {
        "user_id": response.body["userID"],
        "user_name": user_data["user_name"],
        "password": user_data["password"],
    }


@pytest.fixture(scope="session")
def token(client: DemoQaClient, created_user: dict[str, str]) -> str:
    with allure.step("Generate authentication token"):
        response = client.generate_token(
            user_name=created_user["user_name"],
            password=created_user["password"],
        )

    assert response.status_code == 200, response.body
    assert response.body["status"] == "Success", response.body

    return response.body["token"]


@pytest.fixture(scope="session", autouse=True)
def cleanup_user(client: DemoQaClient, created_user: dict[str, str], token: str):
    yield

    with allure.step("Delete all books from user collection"):
        client.delete_all_books(user_id=created_user["user_id"], token=token)

    with allure.step("Delete test user"):
        client.delete_user(user_id=created_user["user_id"], token=token)
