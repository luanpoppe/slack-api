from typing import Annotated
from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import RequestValidationError

from src.application.use_cases.send_command_use_case import SendCommandUseCase
from src.exceptions.validation_exception import ValidationException

from src.communication.requests.request_slack_command import RequestSlackCommand
from src.communication.requests.request_slack_webhook import RequestSlackWebhook
from src.server.handle_commands import HandleCommands

app = FastAPI()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return ValidationException.execute(request, exc)


@app.post("/slack/events")
async def get_root(req: RequestSlackWebhook):
    try:
        if req.type == "url_verification":
            return req.challenge

        if req.type == "event_callback":
            print("\nreq", req)
            # Slack().sendMessage(SlackChannels.geral(), "Respondendo mensagem webhook")
    except Exception as error:
        print("error: ", error)


@app.post("/slack/cmd/init")
async def cmd_init(req: Annotated[RequestSlackCommand, Depends()]):
    handle_commands = HandleCommands()
    return handle_commands.execute(req)
