from dataclasses import dataclass
from typing import Union
from fastapi import Form
from typing_extensions import Annotated


@dataclass
class RequestSlackCommand:
    token: Annotated[Union[str, None], Form()] = None
    team_id: Annotated[Union[str, None], Form()] = None
    team_domain: Annotated[Union[str, None], Form()] = None
    enterprise_id: Annotated[Union[str, None], Form()] = None
    enterprise_name: Annotated[Union[str, None], Form()] = None
    channel_id: Annotated[Union[str, None], Form()] = None
    channel_name: Annotated[Union[str, None], Form()] = None
    user_id: Annotated[Union[str, None], Form()] = None
    user_name: Annotated[Union[str, None], Form()] = None
    command: Annotated[Union[str, None], Form()] = None
    text: Annotated[Union[str, None], Form()] = None
    response_url: Annotated[Union[str, None], Form()] = None
    trigger_id: Annotated[Union[str, None], Form()] = None
    api_app_id: Annotated[Union[str, None], Form()] = None
    is_enterprise_install: Annotated[Union[bool, None], Form()] = None
