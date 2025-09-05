from src.domain.slack.actions_ids_enum import ActionsIdsEnum


class SlackInitialBlock:
    @staticmethod
    def block():
        return [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Welcome to our slack bot! What do you want to do now?",
                    "emoji": True,
                },
            },
            {"type": "divider"},
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "emoji": True,
                            "text": "Create new project",
                        },
                        "value": "click_me_123",
                        "action_id": ActionsIdsEnum.create_new_project(),
                    },
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "emoji": True,
                            "text": "Monitor existing project",
                        },
                        "value": "click_me_123",
                        "action_id": ActionsIdsEnum.monitor_existing_project(),
                    },
                ],
            },
        ]
