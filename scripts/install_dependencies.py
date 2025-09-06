from base_script import BaseScript

BaseScript(["pip-compile requirements.in", "pip-sync"]).execute()
