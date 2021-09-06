from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")

@router.get("/login")
def login(request: Request):
	return templates.TemplateResponse("login.html", {"request": request})
