from pydantic import BaseModel


class FormSelectedUsers(BaseModel):
    type: str
    selected_users: list[str]
