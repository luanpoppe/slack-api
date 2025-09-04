from slack_sdk import WebClient

from handle_env import envs

client = WebClient()
api_response = client.api_test()
print("api_response: ", api_response)
