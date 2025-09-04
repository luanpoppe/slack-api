from fastapi import FastAPI

from lib.slack.channels import SlackChannels
from communication.request_slack_webhook import RequestSlackWebhook
from lib.slack.slack import Slack

app = FastAPI()


@app.post("/slack/events")
async def get_root(req: RequestSlackWebhook):
    try:
        if req.type == "url_verification":
            return req.challenge

        if req.type == "event_callback":
            print("\nreq", req)
            Slack().sendMessage(SlackChannels.geral(), "Respondendo mensagem webhook")
    except Exception as error:
        print("error: ", error)
