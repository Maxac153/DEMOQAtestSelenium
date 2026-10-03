from pydantic import BaseModel


class Date(BaseModel):
    day: str = None
    month: str = None
    year: str = None
    time: str = None
