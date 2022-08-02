from lib2to3.pytree import Base

from pydantic import BaseModel


class Msg(BaseModel):
    msg: str
