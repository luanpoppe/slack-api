from slack_sdk.models.views import View
from slack_sdk.models.blocks import (
    InputBlock,
    PlainTextInputElement,
    PlainTextObject,
    DividerBlock,
    HeaderBlock,
)

from src.domain.slack.enums.modal_ids_enum import ModalIdsEnum


class AnswerProjectFormModal:
    @staticmethod
    def modal(project_id: str, project_name: str):
        modal_view = View(
            type="modal",
            callback_id=ModalIdsEnum().answer_project_form_id(project_id),
            title=f"Answer Project Formulary: {project_name}",
            submit=PlainTextObject(text="Answer", emoji=True),
            close=PlainTextObject(text="Cancel", emoji=True),
            blocks=[
                HeaderBlock(text="Questions:"),
                AnswerProjectFormModal._form_question(1, "Question name 1"),
                AnswerProjectFormModal._form_question(2, "Question name 2"),
                AnswerProjectFormModal._form_question(3, "Question name 3"),
            ],
        )
        return modal_view.to_dict()

    @staticmethod
    def _form_question(question_number: int, question_name: str):
        return InputBlock(
            block_id=f"form_question_block{question_number}",
            label=PlainTextObject(text=question_name, emoji=True),
            element=PlainTextInputElement(
                action_id=f"form_question_input{question_number}",
            ),
        )
