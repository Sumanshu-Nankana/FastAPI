from fastapi import APIRouter, Depends
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from db.repository.jobs import list_jobs
from sqlalchemy.orm import Session
from db.session import get_db

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/")
def home(request:Request, db:Session=Depends(get_db)):
	jobs = list_jobs(db=db)
	return templates.TemplateResponse("jobs/homepage.html", {"request" : request, "jobs" : jobs})
