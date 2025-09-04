from dataclasses import dataclass


@dataclass
class NoEnvException(Exception):
    envName: str

    def __str__(self) -> str:
        return f"Error - Env variable {self.envName} not found"
