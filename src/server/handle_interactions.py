from fastapi import Response
from src.application.use_cases.create_new_project_use_case import (
    CreateNewProjectUseCase,
)
from src.communication.requests.request_slack_interaction import (
    RequestSlackInteraction,
    SlackInteractionPayload,
)
from src.domain.slack.actions_ids_enum import ActionsIdsEnum


class HandleInteractions:

    async def execute(self, req: RequestSlackInteraction):
        body = SlackInteractionPayload.model_validate_json(req.payload)
        print("\nbody", body)
        if (
            body.actions
            and body.actions[0].action_id == ActionsIdsEnum.create_new_project()
        ):
            use_case = CreateNewProjectUseCase()
            return use_case.execute(body)
