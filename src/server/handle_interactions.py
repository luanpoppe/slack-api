from fastapi import Response
from src.communication.requests.request_slack_interaction import (
    RequestSlackInteraction,
    SlackInteractionPayload,
)


class HandleInteractions:
    async def execute(self, req: RequestSlackInteraction):
        print("\nreq", req)
        body = SlackInteractionPayload.model_validate_json(req.payload)
        print("\nbody", body)
        return Response(status_code=200)
        # if req.command == CommandsEnum.init():
        #     use_case = SendCommandUseCase()
        #     return use_case.execute(req)
