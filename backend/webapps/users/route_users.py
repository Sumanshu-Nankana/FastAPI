from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")

@router.get("/register")
def register(request: Request):
	return templates.TemplateResponse("users/users_register.html", {"request" : request})
