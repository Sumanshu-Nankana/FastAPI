from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from models import Items
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")

@router.get("/", tags=["HomePage"])
def home_page(request: Request, db:Session=Depends(get_db)):
	items = db.query(Items).all()
	return templates.TemplateResponse("item_homepage.html", {"request" : request, "items" : items})
