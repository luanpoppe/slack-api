from fastapi import Response, status
from src.communication.requests.request_slack_interaction import SlackInteractionPayload
from src.domain.projects.project_entity import CreateProjectEntity, ProjectEntity
from src.domain.slack.forms.create_new_project import CreateNewProjectForm
from src.lib.slack.slack import Slack
from src.lib.sql_alchemy.repositories.project_repository import ProjectRepository


class SubmitCreateNewProjectUseCase:
    def execute(self, body: SlackInteractionPayload):
        try:
            assert body.view is not None
            assert body.view.state is not None

            form = CreateNewProjectForm(**body.view.state.values).get_values()
            selected_users = form.selected_users

            repository = ProjectRepository()
            entity = CreateProjectEntity(
                name=form.name,
                description=form.description,
                question_one=form.question_1,
                question_two=form.question_2,
                question_three=form.question_3,
            )

            p_entity = ProjectEntity(**entity.__dict__)
            value_created = repository.create(p_entity)

            assert form.conversation_id is not None

            for user in selected_users:
                Slack().sendMessage(
                    user,
                    text=f"Please answer the formulary of the project: {form.name}",
                )

            Slack().sendMessage(
                form.conversation_id,
                f"Project {value_created.name} successfully created",
            )

            return Response(status_code=200)
        except Exception as error:
            print("error: ", error)
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
