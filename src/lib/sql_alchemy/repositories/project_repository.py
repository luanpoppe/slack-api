from dataclasses import dataclass

from src.domain.projects.project_entity import ProjectEntity
from src.lib.sql_alchemy.repositories.base_repository import BaseRepository


@dataclass
class ProjectRepository(BaseRepository[ProjectEntity]):
    def __init__(self):
        super().__init__(entity=ProjectEntity)
