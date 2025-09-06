from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.handle_env import envs

engine = create_engine(envs.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()
