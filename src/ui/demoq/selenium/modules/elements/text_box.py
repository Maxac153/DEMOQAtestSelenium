from pydantic import BaseModel


class TextBox(BaseModel):
    full_name: str = ''
    email: str = ''
    current_address: str = ''
    permanent_address: str = ''
