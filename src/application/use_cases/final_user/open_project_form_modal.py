from src.communication.requests.request_slack_interaction import SlackInteractionPayload
from src.communication.slack_modals.answer_project_form_modal import (
    AnswerProjectFormModal,
)
from src.lib.slack.slack import Slack
from fastapi import Response, status


class ClickCreateNewProjectUseCase:
    def execute(self, payload: SlackInteractionPayload):
        try:
            block = AnswerProjectFormModal.modal("project_id", "project_name")
            Slack().sendOpenModal(payload.trigger_id, view=block)

            return Response(status_code=status.HTTP_200_OK)
        except Exception as error:
            print("error: ", error)
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
