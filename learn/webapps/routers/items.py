from fastapi import APIRouter, Request, Depends, responses, status
from fastapi.templating import Jinja2Templates
from models import Items, User
from sqlalchemy.orm import Session
from database import get_db
from jose import jwt
from config import settings
from datetime import datetime
from typing import Optional

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")


@router.get("/", tags=["HomePage"])
def home_page(request: Request, db: Session = Depends(get_db), msg: str = None):
    items = db.query(Items).all()
    return templates.TemplateResponse(
        "item_homepage.html", {"request": request, "items": items, "msg": msg}
    )


@router.get("/detail/{id}")
def item_detail(request: Request, id: int, db: Session = Depends(get_db)):
    item = db.query(Items).filter(Items.id == id).first()
    email = db.query(User).filter(User.id == item.owner_id).first().email
    return templates.TemplateResponse(
        "item_detail.html", {"request": request, "item": item, "email": email}
    )


@router.get("/update/{id}")
def update_item(id: int, request: Request, db: Session = Depends(get_db)):
    item = db.query(Items).filter(Items.id == id).first()
    return templates.TemplateResponse(
        "update_item.html", {"request": request, "item": item}
    )


@router.get("/create-an-item")
def create_an_item(request: Request):
    return templates.TemplateResponse("create_item.html", {"request": request})


@router.post("/create-an-item")
async def create_an_item(request: Request, db: Session = Depends(get_db)):
    form = await request.form()
    title = form.get("title")
    description = form.get("description")
    errors = []
    if not title or len(title) < 4:
        errors.append("Title should be > 4 chars")
    if not description or len(description) < 10:
        errors.append("Description should be > 10 chars")
    if len(errors) > 0:
        return templates.TemplateResponse(
            "create_item.html", {"request": request, "errors": errors}
        )
    try:
        token = request.cookies.get("access_token")
        if not token:
            errors.append("Kindly Authenticate first by login")
            return templates.TemplateResponse(
                "create_item.html", {"request": request, "errors": errors}
            )
        scheme, _, param = token.partition(" ")
        payload = jwt.decode(param, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        email = payload.get("sub")
        if email is None:
            errors.append("Kindly login first, you are not authenticated")
            return templates.TemplateResponse(
                "create_item.html", {"request": request, "errors": errors}
            )
        else:
            user = db.query(User).filter(User.email == email).first()
            if user is None:
                errors.append("You are not authenticated, Kindly Login")
                return templates.TemplateResponse(
                    "create_item.html", {"request": request, "errors": errros}
                )
            else:
                item = Items(
                    title=title,
                    description=description,
                    date_posted=datetime.now().date(),
                    owner_id=user.id,
                )
                db.add(item)
                db.commit()
                db.refresh(item)
                print(item.id)
                return responses.RedirectResponse(
                    f"/detail/{item.id}", status_code=status.HTTP_302_FOUND
                )
    except Exception as e:
        errors.append("Something is wrong !")
        print(e)
        return templates.TemplateResponse(
            "create_item.html", {"request": request, "errors": errors}
        )


@router.get("/update-delete-item")
def show_items_to_delete(request: Request, db: Session = Depends(get_db)):
    errors = []
    token = request.cookies.get("access_token")
    if token is None:
        errors.append("Kindly Login/Authenticate")
        return templates.TemplateResponse(
            "show_items_to_update_delete.html", {"request": request, "errors": errors}
        )
    else:
        try:
            scheme, _, param = token.partition(" ")
            payload = jwt.decode(
                param, settings.SECRET_KEY, algorithms=settings.ALGORITHM
            )
            email = payload.get("sub")
            user = db.query(User).filter(User.email == email).first()
            items = db.query(Items).filter(Items.owner_id == user.id).all()
            return templates.TemplateResponse(
                "show_items_to_update_delete.html", {"request": request, "items": items}
            )
        except Exception as e:
            print(e)
            errors.append("Something is wrong!!, May be you are not Authenticated")
            return templates.TemplateResponse(
                "show_items_to_update_delete.html",
                {"request": request, "errors": errors},
            )


@router.get("/search")
def search_jobs(request: Request, query: Optional[str], db: Session = Depends(get_db)):
    items = db.query(Items).filter(Items.title.contains(query)).all()
    return templates.TemplateResponse(
        "item_homepage.html", {"request": request, "items": items}
    )
