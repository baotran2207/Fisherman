import email
from os import access
from typing import List, Optional, Protocol

from pydantic import BaseModel, EmailStr

from app.enums import *


class UserBase(BaseModel):
    full_name: Optional[str] = None
    status: Optional[bool] = True
    email: Optional[EmailStr] = None
    status: Optional[int] = Status.Active.value
    phone: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class User(UserBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenPayload(BaseModel):
    sub: Optional[list]
