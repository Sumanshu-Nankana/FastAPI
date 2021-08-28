from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import ItemCreate, ShowItem
from models import Items
from database import get_db
from datetime import datetime
from typing import List

router = APIRouter()

@router.post("/item", tags=["item"], response_model=ShowItem)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
	item = Items(**item.dict(), date_posted = datetime.now().date(), owner_id=1)
	db.add(item)
	db.commit()
	db.refresh(item)
	return item

@router.get("/item/all", tags=["item"], response_model=List[ShowItem])
def get_all_items(db: Session=Depends(get_db)):
	items = db.query(Items).all()
	return items


@router.get("/item/{id}", tags=["item"], response_model=ShowItem)
def get_item_by_id(id:int, db: Session=Depends(get_db)):
	item = db.query(Items).filter(Items.id==id).first()
	if not item:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item with {id} does not exists")
	return item

