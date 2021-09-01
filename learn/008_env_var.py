from fastapi import FastAPI
from config import setting

tags_metadata = [
    {"name": "user", "description": "This is user route"},
    {"name": "products", "description": "This is product route"},
]

app = FastAPI(
    title=setting.TITLE,
    version=setting.VERSION,
    description=setting.DESCRIPTION,
    openapi_tags=tags_metadata,
    contact={"name": setting.NAME, "email": setting.EMAIL},
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
