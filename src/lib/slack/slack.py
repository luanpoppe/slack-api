from typing import Any, Dict, Sequence
from src.handle_env import envs
from slack_sdk import WebClient
from slack_sdk.models.blocks import Block


class Slack:
    _client = WebClient(token=envs.SLACK_BOT_TOKEN)

    def test(self):
        api_response = self._client.api_test()
        print("api_response: ", api_response)

    def sendMessage(
        self,
        channel_id: str,
        text: str | None = None,
        blocks: Sequence[Dict[Any, Any] | Block] | None = None,
    ):
        if (text is None) and (blocks is None):
            raise Exception(
                "To send a message, you must pass a text string or a block string"
            )
        response = self._client.chat_postMessage(
            channel=channel_id, text=text, blocks=blocks
        )

        print("\nresponse", response)

    def sendOpenModal(
        self,
        trigger_id: str,
        view: Any,
    ):
        response = self._client.views_open(trigger_id=trigger_id, view=view)

        print("\nresponse", response)
