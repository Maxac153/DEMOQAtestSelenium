import os

import allure
import requests

from src.api.demoq.request.api.models import ApiResponse


class DemoQaClient:
    def __init__(self, base_url: str = os.environ.get("DEMOQA_HOST")):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )

    def _request(
            self,
            method: str,
            path: str,
            *,
            json: dict[str, any] | None = None,
            params: dict[str, any] | None = None,
            headers: dict[str, str] | None = None,
    ) -> ApiResponse:
        url = f"{self.base_url}{path}"

        with allure.step(f"{method} {url}"):
            if json:
                allure.attach(
                    str(json),
                    name="Request body",
                    attachment_type=allure.attachment_type.JSON,
                )

            response = self.session.request(
                method=method,
                url=url,
                json=json,
                params=params,
                headers=headers,
                timeout=30,
            )

            allure.attach(
                str(response.status_code),
                name="Response status",
                attachment_type=allure.attachment_type.TEXT,
            )

            if response.text:
                allure.attach(
                    response.text,
                    name="Response body",
                    attachment_type=allure.attachment_type.JSON,
                )

        try:
            body = response.json()
        except ValueError:
            body = response.text

        return ApiResponse(
            status_code=response.status_code,
            body=body,
            headers=dict(response.headers),
        )

    def create_user(self, user_name: str, password: str) -> ApiResponse:
        return self._request(
            "POST",
            "/Account/v1/User",
            json={
                "userName": user_name,
                "password": password,
            },
        )

    def generate_token(self, user_name: str, password: str) -> ApiResponse:
        return self._request(
            "POST",
            "/Account/v1/GenerateToken",
            json={
                "userName": user_name,
                "password": password,
            },
        )

    def authorized(self, user_name: str, password: str) -> ApiResponse:
        return self._request(
            "POST",
            "/Account/v1/Authorized",
            json={
                "userName": user_name,
                "password": password,
            },
        )

    def get_books(self) -> ApiResponse:
        return self._request(
            "GET",
            "/BookStore/v1/Books",
        )

    def get_user(self, user_id: str, token: str) -> ApiResponse:
        return self._request(
            "GET",
            f"/Account/v1/User/{user_id}",
            headers={
                "Authorization": f"Bearer {token}",
            },
        )

    def add_book(
            self,
            user_id: str,
            token: str,
            isbn: str,
    ) -> ApiResponse:
        return self._request(
            "POST",
            "/BookStore/v1/Books",
            json={
                "userId": user_id,
                "collectionOfIsbns": [
                    {
                        "isbn": isbn,
                    }
                ],
            },
            headers={
                "Authorization": f"Bearer {token}",
            },
        )

    def delete_book(
            self,
            user_id: str,
            token: str,
            isbn: str,
    ) -> ApiResponse:
        return self._request(
            "DELETE",
            "/BookStore/v1/Book",
            params={
                "ISBN": isbn,
                "UserId": user_id,
            },
            headers={
                "Authorization": f"Bearer {token}",
            },
        )

    def delete_all_books(
            self,
            user_id: str,
            token: str,
    ) -> ApiResponse:
        return self._request(
            "DELETE",
            f"/BookStore/v1/Books?UserId={user_id}",
            headers={
                "Authorization": f"Bearer {token}",
            },
        )

    def delete_user(self, user_id: str, token: str) -> ApiResponse:
        return self._request(
            "DELETE",
            f"/Account/v1/User/{user_id}",
            headers={
                "Authorization": f"Bearer {token}",
            },
        )
