from fastapi import FastAPI, Depends
from config import settings
from database import engine, get_db
from models import Base, User
from schemas import UserCreate
from hashing import Hasher
from sqlalchemy.orm import Session


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


@app.get("/users", tags=["user"])
def get_users():
    return {"message": "hello user"}


@app.get("/items", tags=["products"])
def get_items():
    return {"message": "hello items"}


@app.get("/getenvvar", tags=["config"])
def get_envvars():
    return {"database": setting.DATABASE_URL}


@app.post("/users", tags=["user"])
def create_users(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = Hasher.get_hash_password(user.password)
    user = User(email=user.email, password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
