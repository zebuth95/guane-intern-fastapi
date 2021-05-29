from typing import List
from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from .sql_app import crud, schemas
from .sql_app.database import SessionLocal
from .sql_app.database import get_db
from .sql_app.auth import Auth

app = FastAPI()
security = HTTPBearer()
auth_handler = Auth()

"""
User
"""

@app.post("/user/signup", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post('/login')
def login(user_details: schemas.AuthModel, db: Session = Depends(get_db)):
    user = crud.get_user_by_email(db, email=user.email)
    if (user is None):
        return HTTPException(status_code=401, detail='Invalid username')
    if (not auth_handler.verify_password(user_details.password, user['password'])):
        return HTTPException(status_code=401, detail='Invalid password')

    access_token = auth_handler.encode_token(user['key'])
    refresh_token = auth_handler.encode_refresh_token(user['key'])
    return {'access_token': access_token, 'refresh_token': refresh_token}

@app.get("/user/", response_model=List[schemas.User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)) -> list:
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/user/{id}", response_model=schemas.User)
async def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id_user=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

"""
Dog

"""

@app.post("/dog/", response_model=schemas.Dog)
def create_dog(dog: schemas.DogCreate, db: Session = Depends(get_db)) -> dict:
    return crud.create_dog(db=db, dog=dog)

@app.get("/dog/", response_model=List[schemas.Dog])
def read_dogs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    dogs = crud.get_dogs(db, skip=skip, limit=limit)
    return dogs

@app.get("/dog/{id}", response_model=schemas.Dog)
def read_dog(id: int, db: Session = Depends(get_db)):
    db_dog = crud.get_dog(db, id_user=id)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return db_dog

@app.post("/dog/{name}", response_model=schemas.Dog)
def get_dog_by_name(name: str, db: Session = Depends(get_db)):
    db_dog = crud.get_dog_by_name(db, name=name)
    if db_dog is None:
        raise HTTPException(status_code=404, detail="Dog not found")
    return db_dog

