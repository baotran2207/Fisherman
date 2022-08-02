import logging
from functools import lru_cache
from typing import Dict, Type

from pydantic import PostgresDsn, SecretStr

from app.core.settings.app import AppSettings
from app.core.settings.base import BaseAppSettings
from app.core.settings.enums import AppEnv


class DevAppSettings(AppSettings):
    debug: bool = True

    title: str = "Dev FastAPI example application"

    logging_level: int = logging.DEBUG

    class Config(AppSettings.Config):
        env_file = ".env"


class TestAppSettings(AppSettings):
    debug: bool = True

    title: str = "Test FastAPI example application"

    secret_key: SecretStr = SecretStr("test_secret")

    database_url: PostgresDsn
    max_connection_count: int = 5
    min_connection_count: int = 5

    logging_level: int = logging.DEBUG


class ProdAppSettings(AppSettings):
    class Config(AppSettings.Config):
        env_file = "prod.env"


environement: Dict[AppEnv, Type[AppSettings]] = {
    AppEnv.dev: DevAppSettings,
    AppEnv.prod: None,
    AppEnv.test: None,
}


@lru_cache
def get_app_settings() -> AppSettings:
    app_env = BaseAppSettings().app_env
    config = environement[app_env]
    return config()
