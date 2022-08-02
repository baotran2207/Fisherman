from typing import Optional, Type, TypeVar
from xmlrpc.client import Boolean

from passlib.context import CryptContext
from pydantic import EmailStr
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.db.base_class import Base
from app.models.user import User

password_context = CryptContext(schemes=["bcrypt"], deprecated=["auto"])


def hash_password(password: str) -> str:
    return password_context.hash(password)


ModelType = TypeVar("ModelType", bound=Base)


class CRUDUser(CRUDBase[User]):
    def __init__(self, model: Type[ModelType]) -> None:
        self.model = model

    def get_by_email(self, db: Session, email: EmailStr) -> Optional[ModelType]:
        return db.query(self.model).filter(self.model.email == email).first()

    def create(self, db: Session, *, obj_to_create: ModelType) -> User:

        hashed_pass = hash_password(obj_to_create.password)
        db_obj = User(
            email=obj_to_create.email,
            full_name=obj_to_create.full_name,
            hashed_password=hash_password(obj_to_create.password),
        )

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


user = CRUDUser(User)
