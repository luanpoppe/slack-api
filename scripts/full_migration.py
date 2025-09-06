from base_script import BaseScript

BaseScript(["alembic revision --autogenerate", "alembic upgrade head"]).execute()
