from fastapi import APIRouter, Depends
from schemas import UserCreate, ShowUser
from sqlalchemy.orm import Session
from models import User
from hashing import Hasher
from database import get_db

router = APIRouter()


@router.post("/user", tags=["user"], response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    user = User(email=user.email, password=Hasher.get_hash_password(user.password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
