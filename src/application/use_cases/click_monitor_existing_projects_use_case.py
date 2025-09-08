from fastapi import Response, status
from src.communication.requests.request_slack_interaction import SlackInteractionPayload
from src.lib.slack.slack import Slack
from src.lib.sql_alchemy.repositories.project_repository import ProjectRepository


class ClickMonitorExistingProjectsUseCase:
    def execute(self, body: SlackInteractionPayload):
        try:
            assert body.channel is not None
            assert body.channel.id is not None

            repo = ProjectRepository()
            all_projects = repo.get_all()
            all_projects_formatted = [
                f"Name: {p.name} - Id: {p.id}" for p in all_projects
            ]

            Slack().sendMessage(
                body.channel.id,
                text=f"Projetos são esses: {"\n".join(all_projects_formatted)}",
            )
            return Response(status_code=status.HTTP_200_OK)
        except Exception as error:
            print("error: ", error)
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
