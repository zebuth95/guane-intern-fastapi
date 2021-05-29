from typing import List, Optional

from pydantic import BaseModel, Field

class DogBase(BaseModel):
    name: str
    picture: Optional[str] = None

class DogCreate(DogBase):
    id_user: int

class Dog(DogBase):
    id: int
    is_adopted: bool

    class Config:
        orm_mode: True

class UserBase(BaseModel):
    name: str
    last_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    dogs: List[Dog] = []

    class Config:
        orm_mode = True

class AuthModel(BaseModel):
    name: str
    password: str