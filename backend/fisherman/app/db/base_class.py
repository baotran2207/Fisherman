from email.policy import default
from typing import Any

from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
import uuid as uuid_pkg

@as_declarative()
class Base:
    # id: Any
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


# class Base(MinBase):
#     pass
    # created_at = Column(DateTime(timezone=True), default=func.now())
    # lastchanged_at = Column(DateTime(timezone=True), onupdate=func.now())
    # uuid: uuid_pkg.UUID = Column(
    #     default_factory=uuid_pkg.uuid4,
    #     primary_key=True,
    #     index=True,
    #     nullable=False,
    # )
