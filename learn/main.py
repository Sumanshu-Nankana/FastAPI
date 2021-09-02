from fastapi import FastAPI, Depends
from config import settings
from database import engine, get_db
from models import Base, User
from schemas import UserCreate
from hashing import Hasher
from sqlalchemy.orm import Session
from routers import users, items, login
from webapps.routers import items as web_items

desc = """
This is project description
"""

tags_metadata = [
    {"name": "user", "description": "This is user route"},
    {"name": "products", "description": "This is product route"},
]


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_TITLE,
    version=settings.PROJECT_VERSION,
    description=desc,
    openapi_tags=tags_metadata,
    contact={"name": "Sumanshu Nankana", "email": "sumanshunankana@gmail.com"},
    redoc_url=None,
)

# we can pass the prefix argument as well
app.include_router(users.router)
app.include_router(items.router)
app.include_router(login.router)
app.include_router(web_items.router)
