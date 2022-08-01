import logging
import sys
from types import FrameType


from loguru import logger
from typing import Any, Dict, List, Tuple, Optional, cast

from pydantic import PostgresDsn, SecretStr, validator, HttpUrl

from app.core.settings.base import BaseAppSettings


class BaseHandler(logging.Handler):

    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)
        frame ,depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(
            depth=depth, exception=record.exc_info
        ).log(level, record.getMessage())


class AppSettings(BaseAppSettings):


    # DB
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, val: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(val, str):
            return val
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    # logging
    logging_level:int  = logging.info
    loggers: Tuple[str, str] =  ("uvicorn.asgi", "uvicorn.access")

    def configure_logging(self) -> None:
        logging.getLogger().handlers = [BaseHandler()]
        for logger_name in self.loggers:
            logging_logger = logging.getLogger(logger_name)
            logging_logger.handlers = [BaseHandler(level=self.logging_level)]

        logger.configure(handlers=[{"sink": sys.stderr, "level": self.logging_level}])

    # Security
    secret_key: SecretStr
    jwt_token_prefix: str = "Token" # token? Bearer ?


    # sentry
    SENTRY_DSN: Optional[HttpUrl] = None

    @validator("SENTRY_DSN", pre=True)
    def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
        if len(v) == 0:
            return None
        return v


    # fastapi only
    debug: bool = False
    docs_url: str = "/docs"
    openapi_prefix: str = ""
    openapi_url: str = "/openapi.json"
    redoc_url: str = "/redoc"
    title = 'Fisherman'

    @property
    def fastapi_kwargs(self) -> Dict[str, Any]:
        return {
            "debug": self.debug,
            "docs_url": self.docs_url,
            "openapi_prefix": self.openapi_prefix,
            "openapi_url": self.openapi_url,
            "redoc_url": self.redoc_url,
            "title": self.title,
        }