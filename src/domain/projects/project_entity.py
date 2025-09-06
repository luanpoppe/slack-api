from sqlalchemy import Column, Integer, String

from src.lib.sql_alchemy.engine import Base


class Projects(Base):
    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
