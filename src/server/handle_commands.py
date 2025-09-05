from src.application.use_cases.send_command_use_case import SendCommandUseCase
from src.communication.requests.request_slack_command import RequestSlackCommand
from src.domain.slack.commands_enum import CommandsEnum


class HandleCommands:
    def execute(self, req: RequestSlackCommand):
        if req.command == CommandsEnum.init():
            use_case = SendCommandUseCase()
            return use_case.execute(req)
