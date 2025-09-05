from src.communication.requests.request_slack_command import RequestSlackCommand
from src.communication.requests.request_slack_interaction import SlackInteractionPayload
from src.communication.slack_blocks.initial_block import SlackInitialBlock
from src.lib.slack.channels import SlackChannels
from src.lib.slack.slack import Slack
from fastapi import Response, status


class CreateNewProjectUseCase:
    def execute(self, payload: SlackInteractionPayload):
        try:
            print("\nreq", payload)
            block = SlackInitialBlock.block()
            Slack().sendMessage(SlackChannels.geral(), blocks=block)
            return Response(status_code=status.HTTP_200_OK)
        except Exception as error:
            print("error: ", error)
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
