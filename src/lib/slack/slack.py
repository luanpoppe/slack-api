from handle_env import envs
from slack_sdk import WebClient


class Slack:
    client = WebClient(token=envs.SLACK_BOT_TOKEN)

    def test(self):
        api_response = self.client.api_test()
        print("api_response: ", api_response)

    def sendMessage(self, channel_id: str, text: str):
        response = self.client.chat_postMessage(channel=channel_id, text=text)

        print("\nresponse", response)
