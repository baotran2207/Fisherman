from email.policy import default
from operator import index
from app.db.base_class import Base

from sqlalchemy import Boolean,Column,Integer, String, column
from sqlalchemy.orm import relationship

from app.enums import *


class User(Base):
    email = Column(Integer, primary_key=True, index=True)
    phone = Column(String, index=True)
    full_name = Column(String, index=True)
    hashed_password = Column(String)

    status = Column(Integer, default=Status.Active.value)
    is_superuser = Column(Boolean(), default = False)
