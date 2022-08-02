from enum import Enum


class AppEnv(Enum):
    prod: str = "prod"
    dev: str = "dev"
    test: str = "test"
