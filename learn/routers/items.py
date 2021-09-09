from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import ItemCreate, ShowItem
from models import Items, User
from database import get_db
from datetime import datetime
from typing import List, Optional
from fastapi.encoders import jsonable_encoder
from routers.login import oauth2_scheme
from jose import jwt
from config import settings

router = APIRouter()


def get_user_from_token(db, token):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        username = payload.get("sub")
        if not username:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate Credentials",
            )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate Credetials",
        )
    user = db.query(User).filter(User.email == username).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    return user


@router.post("/item", tags=["item"], response_model=ShowItem)
def create_item(
    item: ItemCreate, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    user = get_user_from_token(db, token)
    owner_id = user.id
    item = Items(**item.dict(), date_posted=datetime.now().date(), owner_id=owner_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item


@router.get("/item/all", tags=["item"], response_model=List[ShowItem])
def get_all_items(db: Session = Depends(get_db)):
    items = db.query(Items).all()
    return items


@router.get("/item/autocomplete")
def autocomplete(term: Optional[str] = None, db: Session = Depends(get_db)):
    items = db.query(Items).filter(Items.title.contains(term)).all()
    suggestions = []
    for item in items:
        suggestions.append(item.title)
    return suggestions


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
def update_item_by_id(
    id: int,
    item: ItemCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    user = get_user_from_token(db, token)
    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return {"message": f"No Details found for Item ID {id}"}
    if existing_item.first().owner_id == user.id:
        existing_item.update(jsonable_encoder(item))
        db.commit()
        return {"message": f"Details successfully updated for Item ID {id}"}
    else:
        return {"message": "You are not authorized"}


# Method-2
@router.put("/item/update1/{id}", tags=["item"])
def update1_item_by_id(
    id: int,
    item: ItemCreate,
    db: Session = Depends(get_db),
    token: str = Depends(oauth2_scheme),
):
    user = get_user_from_token(db, token)
    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return {"message": f"No Details found for Item ID {id}"}
    if existing_item.first().owner_id == user.id:
        existing_item.update(item.__dict__)
        db.commit()
        return {"message": f"Details successfully updated for Item ID {id}"}
    else:
        return {"message": "You are not authorized"}


@router.delete("/item/delete/{id}", tags=["item"])
def delete_item_by_id(
    id: int, db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    user = get_user_from_token(db, token)
    existing_item = db.query(Items).filter(Items.id == id)
    if not existing_item.first():
        return {"message": f"No Details found for Item ID {id}"}
    if existing_item.first().owner_id == user.id:
        existing_item.delete()
        db.commit()
        return {"message": f"Item ID {id} has been successfully deleted"}
    else:
        return {"message": "You are not authorized"}
