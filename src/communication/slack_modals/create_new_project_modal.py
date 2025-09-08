from slack_sdk.models.views import View
from slack_sdk.models.blocks import (
    InputBlock,
    PlainTextInputElement,
    PlainTextObject,
    DividerBlock,
    HeaderBlock,
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

        print(
            "\nModalIdsEnum.create_new_project_id", ModalIdsEnum.create_new_project_id
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
