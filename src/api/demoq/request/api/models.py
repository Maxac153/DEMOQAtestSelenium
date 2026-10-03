from typing import Any

from pydantic import BaseModel


class ApiResponse(BaseModel):
    status_code: int
    body: Any
    headers: dict[str, str]
