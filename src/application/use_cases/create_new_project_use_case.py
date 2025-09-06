import json
from src.communication.requests.request_slack_interaction import SlackInteractionPayload
from src.communication.slack_modals.create_new_project_modal import (
    CreateNewProjectModal,
)
from src.lib.slack.slack import Slack
from fastapi import Response, status


class CreateNewProjectUseCase:
    def execute(self, payload: SlackInteractionPayload):
        try:
            print("\nreq", payload)
            block = CreateNewProjectModal.modal()
            Slack().sendOpenModal(payload.trigger_id, view=block)
            return Response(status_code=status.HTTP_200_OK)
        except Exception as error:
            print("error: ", error)
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
