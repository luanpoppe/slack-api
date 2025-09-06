from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Projects(Base):
    __tablename__ = "projects"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
