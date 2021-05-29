from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False)
    last_name = Column(String, unique=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    dogs = relationship("Dog", back_populates="users")

class Dog(Base):
    __tablename__ = "dogs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=False)
    picture = Column(String, unique=False)
    is_adopted = Column(Boolean, default=True)
    create_date = Column(DateTime(timezone=True), server_default=func.now())
    id_user = Column(Integer, ForeignKey("users.id"))

    users = relationship("User", back_populates="dogs")