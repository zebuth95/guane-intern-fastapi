import ast
import requests
from sqlalchemy.orm import Session
from . import models, schemas
from .auth import Auth

auth_handler = Auth()

"""
User
"""
def get_user(db: Session, id_user: int):
    return db.query(models.User).filter(models.User.id == id_user).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth_handler.encode_password(user.password)
    db_user = models.User(name= user.name, last_name= user.last_name, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.user.id == id)
    if db_user:
        db_user.name = user.name
        db_user.last_name = user.last_name
        db_user.email = user.email
        db_user.is_active = user.is_active
        db.commit()
        db.refresh(db_user)
        return db_user
    else:
        return None

def dog_delete(db: Session, id: int):
    db_dog = db.query(mdoels.User).filter(models.User.id == id)
    if db_user:
        db.delete(db_user)
        db.commit()
    return None

"""
Dog
"""
def get_dog(db: Session, dog_id: int):
    return db.query(models.Dog).filter(models.Dog.id == dog_id).first()

def get_dog_by_name(db: Session, name: str):
    return db.query(models.Dog).filter(models.Dog.name == name).first()

def get_dogs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dog).offset(skip).limit(limit).all()

def create_dog(db: Session, dog: schemas.DogCreate):
    url = "https://dog.ceo/api/breeds/image/random"
    dog.picture = requests.request("GET", url).json()['message']
    db_dog = models.Dog(**dog.dict())
    db.add(db_dog)
    db.commit()
    db.refresh(db_dog)
    return db_dog

def update_dog(db: Session, id: int, dog: schemas.DogCreate):
    db_dog = db.query(models.Dog).filter(models.Dog.id == id)
    if db_dog:
        db_dog.name = dog.name
        db_dog.picture = dog.picture
        db_dog.is_adopted = dog.is_adopted
        db_dog.id_user = dog.id_user
        db.commit()
        db.refresh(db_dog)
        return db_dog
    else:
        return None

def dog_delete(db: Session, id: int):
    db_dog = db.query(mdoels.Dog).filter(models.Dog.id == id)
    if db_dog:
        db.delete(db_dog)
        db.commit()
    return None