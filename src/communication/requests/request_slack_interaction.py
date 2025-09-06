from dataclasses import dataclass
from typing import Literal, Union
from fastapi import Form
from pydantic import BaseModel
from typing_extensions import Annotated


@dataclass
class SlackUser(BaseModel):
    id: str | None = None
    username: str | None = None
    name: str | None = None
    team_id: str | None = None


@dataclass
class SlackChannel(BaseModel):
    id: str | None = None
    name: str | None = None


@dataclass
class SlackActionsText(BaseModel):
    type: str | None = None
    text: str | None = None
    emoji: bool | None = None


@dataclass
class SlackActions(BaseModel):
    action_id: str | None = None
    block_id: str | None = None
    value: str | None = None
    type: str | None = None
    action_ts: str | None = None
    text: SlackActionsText | None = None


@dataclass
class SlackInteractionPayload(BaseModel):
    type: Literal["block_actions", "interactive_message"] | None = None
    user: SlackUser
    channel: SlackChannel | None = None
    trigger_id: str
    actions: list[SlackActions] | None = None


@dataclass
class RequestSlackInteraction:
    payload: Annotated[str, Form()]
