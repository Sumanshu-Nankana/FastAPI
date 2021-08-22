from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.users import UserCreate
from db.session import get_db
from db.repository.users import create_new_user

router = APIRouter()

@router.post("/")
def create_user(user: UserCreate, db: Session=Depends(get_db)):
	user = create_new_user(user, db)
	return user

