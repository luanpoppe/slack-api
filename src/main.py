from lib.slack.channels import SlackChannels
from lib.slack.slack import Slack


slack = Slack()

slack.test()
slack.sendMessage(SlackChannels.geral(), "Opa")
