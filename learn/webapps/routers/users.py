from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/register")
def registration(request:Request):
	return templates.TemplateResponse("user_register.html", {"request":request})
