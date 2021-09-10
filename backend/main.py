from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base import Base
from apis.base import api_router
from webapps.base import api_router as webapp_router
from fastapi.staticfiles import StaticFiles
from fastapi_pagination import add_pagination


# we can pass the metadata information for API
# some fields are of type string and some are of type dictionary (example - contact)
# https://fastapi.tiangolo.com/tutorial/metadata/
# title = title of the API
# version = version of the API. This is the version of your application, not of OpenAPI
# we can see all this metadata information on /docs path of application
# http://localhost:8000/docs


def create_tables():
    Base.metadata.create_all(bind=engine)


description = """
Hello World API
## Heading
**Return JSON format of Hello World **
"""


def include_router(app):
    app.include_router(api_router)
    app.include_router(webapp_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")


def start_application():
    app = FastAPI(
        title=settings.PROJECT_TITLE,
        version=settings.PROJECT_VERSION,
        description=description,
        contact={"name": "Sumanshu Nankana", "email": "sumanshunankana@gmail.com"},
    )
    create_tables()
    include_router(app)
    configure_static(app)
    return app


app = start_application()
