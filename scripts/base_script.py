from dataclasses import dataclass
import os


@dataclass
class BaseScript:
    commands: list[str]

    def execute(self):
        for command in self.commands:
            print(f"Starting command: {command}")
            os.system(command)
            print("Command finished\n\n")
