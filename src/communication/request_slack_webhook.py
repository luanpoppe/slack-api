from pydantic import BaseModel
from typing import Literal

from domain.slack.slack_webook_event import EventSlack


class RequestSlackWebhook(BaseModel):
    type: Literal["url_verification", "event_callback"]
    token: str | None = None
    challenge: str | None = None

    team_id: str | None = None
    api_app_id: str | None = None
    event: EventSlack | None = None
    event_id: str | None = None
    event_time: int | None = None
    authed_users: list[str] | None = None
