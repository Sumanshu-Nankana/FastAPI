from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(include_in_schema=False)
templates = Jinja2Templates(directory="templates")

@router.get("/", tags=["HomePage"])
def home_page(request: Request):
	return templates.TemplateResponse("item_homepage.html", {"request" : request})
