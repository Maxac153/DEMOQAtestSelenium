from pydantic import BaseModel


class Color(BaseModel):
    color_name: list = None
