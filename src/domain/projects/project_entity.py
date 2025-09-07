from dataclasses import dataclass
from sqlalchemy import Column, Integer, String

from src.lib.sql_alchemy.engine import Base


@dataclass
class CreateProjectEntity:
    name: str
    description: str
    question_one: str
    question_two: str
    question_three: str
    id: str | None = None


class ProjectEntity(Base):
    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=True)
    question_one = Column(String(500), nullable=True)
    question_two = Column(String(500), nullable=True)
    question_three = Column(String(500), nullable=True)
