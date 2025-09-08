from slack_sdk.models.views import View
from slack_sdk.models.blocks import (
    InputBlock,
    PlainTextInputElement,
    PlainTextObject,
    DividerBlock,
    HeaderBlock,
    ConversationSelectElement,
    UserMultiSelectElement,
)

from src.domain.slack.enums.modal_ids_enum import ModalIdsEnum


class CreateNewProjectModal:
    @staticmethod
    def modal():
        project_name_input = InputBlock(
            block_id="project_name_block",  # ID único para este bloco
            label=PlainTextObject(text="Project name", emoji=True),
            element=PlainTextInputElement(
                action_id="project_name_input",  # ID único para este campo de texto
                # placeholder=PlainTextObject(text="Ex: Lançamento do App de Vendas"),
            ),
        )

        project_description_input = InputBlock(
            block_id="project_description_block",  # ID único e diferente do primeiro
            label=PlainTextObject(text="Project Description", emoji=True),
            element=PlainTextInputElement(
                action_id="project_description_input",  # ID único e diferente do primeiro
                multiline=True,
                # placeholder=PlainTextObject(
                #     text="Descreva os objetivos principais deste projeto."
                # ),
            ),
        )

        select_conversation = InputBlock(
            block_id=f"select_conversation_block",
            label=PlainTextObject(text="Select conversation", emoji=True),
            element=ConversationSelectElement(
                response_url_enabled=True,
                default_to_current_conversation=True,
                action_id="select_conversation_input",
            ),
        )

        select_users = InputBlock(
            block_id=f"select_users_block",
            label=PlainTextObject(text="Select users", emoji=True),
            element=UserMultiSelectElement(
                placeholder="Select users to be notified",
                action_id="select_users_input",
            ),
        )

        modal_view = View(
            type="modal",
            callback_id=ModalIdsEnum.create_new_project_id,
            title="Create New Project",
            submit=PlainTextObject(text="Create", emoji=True),
            close=PlainTextObject(text="Cancel", emoji=True),
            blocks=[
                project_name_input,
                project_description_input,
                DividerBlock(),
                HeaderBlock(text="Form Questions:"),
                CreateNewProjectModal._form_question(1),
                CreateNewProjectModal._form_question(2),
                CreateNewProjectModal._form_question(3),
                DividerBlock(),
                select_conversation,
                select_users,
            ],
        )
        return modal_view.to_dict()

    @staticmethod
    def _form_question(question_number: int):
        return InputBlock(
            block_id=f"form_question_block{question_number}",
            label=PlainTextObject(text=f"Question {question_number}", emoji=True),
            element=PlainTextInputElement(
                action_id=f"form_question_input{question_number}",
            ),
        )
