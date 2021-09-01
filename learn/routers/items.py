from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import ItemCreate, ShowItem
from models import Items
from database import get_db
from datetime import datetime
from typing import List
from fastapi.encoders import jsonable_encoder
from routers.login import oauth2_scheme

router = APIRouter()


@router.post("/item", tags=["item"], response_model=ShowItem)
def create_item(
    item: ItemCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    item = Items(**item.dict(), date_posted=datetime.now().date(), owner_id=3)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/item/all", tags=["item"], response_model=List[ShowItem])
def get_all_items(db: Session = Depends(get_db)):
    items = db.query(Items).all()
    return items


@router.get("/item/{id}", tags=["item"], response_model=ShowItem)
def get_item_by_id(id: int, db: Session = Depends(get_db)):
    item = db.query(Items).filter(Items.id == id).first()
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with {id} does not exists",
        )
    return item


# Method-1
@router.put("/item/update/{id}", tags=["item"])
def update_item_by_id(id: int, item: ItemCreate, db: Session = Depends(get_db)):
    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return {"message": f"No Details found for Item ID {id}"}
    existing_item.update(jsonable_encoder(item))
    db.commit()
    return {"message": f"Details successfully updated for Item ID {id}"}


# Method-2
@router.put("/item/update1/{id}", tags=["item"])
def update1_item_by_id(id: int, item: ItemCreate, db: Session = Depends(get_db)):
    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return {"message": f"No details found for Item ID {id}"}
    existing_item.update(item.__dict__)
    db.commit()
    return {"message": f"Details successfully updated for Item ID {id}"}


@router.delete("/item/delete/{id}", tags=["item"])
def delete_item_by_id(id: int, db: Session = Depends(get_db)):
    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return {"message": f"No Details found for Item ID {id}"}
    existing_item.delete()
    db.commit()
    return {"message": f"Item ID {id} has been successfully deleted"}
