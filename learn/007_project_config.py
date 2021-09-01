from fastapi import FastAPI
from config import settings


# We can configure documentation user interfaces.

# By default, Swagger UI served at /docs
# we can change Swagger UI URL by using parameter docs_url
# You can disable it by setting docs_url=None

# and ReDoc served at /redoc
# we can change Swagger UI URL by using parameter docs_url
# You can disable it by setting redoc_url=None

app = FastAPI(
    docs_url="/documentation",
    redoc_url="/redocumentation",
    title=settings.PROJECT_TITLE,
    version=settings.PROJECT_VERSION,
)


# we can use our own tags using 'tags' parameter
@app.get("/users", tags=["users"])
def hello_api():
    return {"detail": "hello user"}


# we can use our own tags using 'tags' parameter
@app.get("/items", tags=["items"])
def hello_api():
    return {"detail": "hello item"}
