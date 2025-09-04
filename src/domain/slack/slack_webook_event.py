from typing import Literal
from pydantic import BaseModel


class EventSlack(BaseModel):
    type: Literal["app_mention"] | None = None
    user: str | None = None
    text: str | None = None
    ts: str | None = None
    channel: str | None = None
    event_ts: str | None = None
