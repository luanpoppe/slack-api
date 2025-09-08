from pydantic import BaseModel


class FormSelectedConversation(BaseModel):
    type: str
    selected_conversation: str
