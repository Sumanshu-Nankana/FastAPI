from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas import ItemCreate, ShowItem
from models import Items
from database import get_db
from datetime import datetime

router = APIRouter()

@router.post("/item", tags=["item"], response_model=ShowItem)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
	item = Items(**item.dict(), date_posted = datetime.now().date(), owner_id=1)
	db.add(item)
	db.commit()
	db.refresh(item)
	return item
