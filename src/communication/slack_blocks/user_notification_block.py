from slack_sdk.models.blocks import (
    InputBlock,
    PlainTextInputElement,
    PlainTextObject,
    DividerBlock,
    HeaderBlock,
    ConversationSelectElement,
    UserMultiSelectElement,
    Block,
    ActionsBlock,
    ButtonElement,
)

from src.domain.slack.forms.create_new_project import CreateNewProjectFormFormated


class UserNotificationBlock:
    @staticmethod
    def block(form: CreateNewProjectFormFormated):
        return [
            HeaderBlock(
                text=f"Please answer the formulary of the project: {form.name}"
            ),
            ActionsBlock(
                elements=[
                    ButtonElement(
                        text="Click here",
                        action_id=f"user_notification_{form.name}",
                        value="test value",
                    )
                ]
            ),
        ]
