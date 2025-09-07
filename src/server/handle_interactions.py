from fastapi import Response
from src.application.use_cases.create_new_project_use_case import (
    CreateNewProjectUseCase,
)
from src.communication.requests.request_slack_interaction import (
    RequestSlackInteraction,
    SlackInteractionPayload,
)
from src.domain.projects.project_entity import CreateProjectEntity, ProjectEntity
from src.domain.slack.actions_ids_enum import ActionsIdsEnum
from src.domain.slack.forms.create_new_project import CreateNewProjectForm
from src.lib.sql_alchemy.repositories.project_repository import ProjectRepository


class HandleInteractions:

    async def execute(self, req: RequestSlackInteraction):
        body = SlackInteractionPayload.model_validate_json(req.payload)
        print("\nbody", body)
        if body.type == "view_submission":
            if not body.view or not body.view.state:
                return
            form = CreateNewProjectForm(**body.view.state.values).get_values()
            print("\nform", form)

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
            print("\nvalue_created", value_created)

            return Response(status_code=200)

        elif not body.actions:
            return Response(status_code=400)

        elif body.type == "block_actions":
            if body.actions[0].action_id == ActionsIdsEnum.create_new_project():
                use_case = CreateNewProjectUseCase()
                return use_case.execute(body)
