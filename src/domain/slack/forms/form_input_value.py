from pydantic import BaseModel


class FormInputValue(BaseModel):
    type: str
    value: str
