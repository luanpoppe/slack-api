from fastapi import Response
from src.application.use_cases.click_create_new_project_use_case import (
    ClickCreateNewProjectUseCase,
)
from src.application.use_cases.submit_create_new_project_use_case import (
    SubmitCreateNewProjectUseCase,
)
from src.communication.requests.request_slack_interaction import (
    RequestSlackInteraction,
    SlackInteractionPayload,
)
from src.domain.slack.enums.actions_ids_enum import ActionsIdsEnum
from src.domain.slack.enums.modal_ids_enum import ModalIdsEnum


class HandleInteractions:

    async def execute(self, req: RequestSlackInteraction):
        body = SlackInteractionPayload.model_validate_json(req.payload)

        if body.type == "view_submission":
            if not body.view or not body.view.state:
                return

            if body.view.callback_id == ModalIdsEnum.create_new_project_id:
                use_case = SubmitCreateNewProjectUseCase()
                return use_case.execute(body)

        elif not body.actions:
            return Response(status_code=400)

        elif body.type == "block_actions":
            if body.actions[0].action_id == ActionsIdsEnum.create_new_project():
                use_case = ClickCreateNewProjectUseCase()
                return use_case.execute(body)
            else:
                return Response(status_code=400)
        else:
            return Response(status_code=500)
