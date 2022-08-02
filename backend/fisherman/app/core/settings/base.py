from pydantic import BaseSettings

from app.core.settings.enums import AppEnv


class BaseAppSettings(BaseSettings):

    app_env: AppEnv = AppEnv.dev  ## no default ?

    class Config:
        env_file = ".env"
