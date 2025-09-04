from dataclasses import dataclass
from dotenv import load_dotenv
import os

from exceptions.no_env_exception import NoEnvException

load_dotenv()


@dataclass
class Envs:
    SLACK_BOT_TOKEN: str = ""


envs = Envs()

try:
    keys = envs.__dict__.keys()
    for key in keys:
        env_value = os.getenv(key)
        if env_value == None:
            raise NoEnvException(key)
        envs.__setattr__(key, env_value)

except Exception as error:
    print("error: ", error)
    raise error
