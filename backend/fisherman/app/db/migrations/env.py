import pathlib
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

sys.path.append(str(pathlib.Path(__file__).resolve().parents[3]))

from app.core.config import get_app_settings  # isort:skip
from app.db.base import Base  # noqa



SETTINGS = get_app_settings()
SQLALCHEMY_DATABASE_URI = SETTINGS.SQLALCHEMY_DATABASE_URI

config = context.config

fileConfig(config.config_file_name)  # type: ignore

target_metadata = Base.metadata

config.set_main_option("sqlalchemy.url", str(SQLALCHEMY_DATABASE_URI))


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


run_migrations_online()
