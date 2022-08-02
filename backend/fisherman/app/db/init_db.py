from loguru import logger
from sqlalchemy.orm import Session

# from app import crud, schemas
from app.core.config import get_app_settings
from app.crud import user
from app.db import base
from app.db.session import SessionLocal
from app.schemas import UserCreate


def init_db(db: Session, settings=get_app_settings()):
    first_user = user.get_by_email(db, email=settings.WEBMASTER_EMAIL)

    if not first_user:
        init_user = UserCreate(
            email=settings.WEBMASTER_EMAIL,
            password=settings.WEBMASTER_PASSWORD,
            is_superuser=True,
        )
        new_user = user.create(db, obj_to_create=init_user)  # noqa: F841
        logger.info("created", new_user)

    logger.info("The first user was created ")
    return first_user


if __name__ == "__main__":
    db = SessionLocal()
    settings = get_app_settings()
    init_db(db, settings)
