from fastapi import FastAPI
from config import settings
from database import engine
from models import Base


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


@app.post("/users", target=["users"])
def create_users():
    pass
