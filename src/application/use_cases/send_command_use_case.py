import json
from src.communication.requests.request_slack_command import RequestSlackCommand
from src.lib.slack.channels import SlackChannels
from src.lib.slack.slack import Slack
from fastapi import Response, status


class SendCommandUseCase:
    def execute(self, req: RequestSlackCommand):
        try:
            print("\nreq", req)
            block = {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "You have a new request:\n*<fakeLink.toEmployeeProfile.com|Fred Enriquez - New device request>*",
                        },
                    },
                    {
                        "type": "section",
                        "fields": [
                            {"type": "mrkdwn", "text": "*Type:*\nComputer (laptop)"},
                            {"type": "mrkdwn", "text": "*When:*\nSubmitted Aut 10"},
                            {
                                "type": "mrkdwn",
                                "text": "*Last Update:*\nMar 10, 2015 (3 years, 5 months)",
                            },
                            {
                                "type": "mrkdwn",
                                "text": "*Reason:*\nAll vowel keys aren't working.",
                            },
                            {
                                "type": "mrkdwn",
                                "text": '*Specs:*\n"Cheetah Pro 15" - Fast, really fast"',
                            },
                        ],
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "emoji": True,
                                    "text": "Approve",
                                },
                                "style": "primary",
                                "value": "click_me_123",
                            },
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "emoji": True,
                                    "text": "Deny",
                                },
                                "style": "danger",
                                "value": "click_me_123",
                            },
                        ],
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "Click Me",
                                    "emoji": True,
                                },
                                "value": "click_me_123",
                                "action_id": "actionId-0",
                            }
                        ],
                    },
                ]
            }
            Slack().sendMessage(SlackChannels.geral(), json.dumps(block))
            return Response(status_code=status.HTTP_200_OK)
        except Exception as error:
            print("error: ", error)
            return Response(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
