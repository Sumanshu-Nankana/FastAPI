from fastapi import FastAPI
from core.config import settings
from db.session import engine
from db.base_class import Base

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

def start_application():
	app = FastAPI(title=settings.PROJECT_TITLE,
			 version=settings.PROJECT_VERSION,
             description=description,
			 contact={
			 "name" : "Sumanshu Nankana",
			 "email" : "sumanshunankana@gmail.com"
			 }
			 )
	create_tables()
	return app


app = start_application()

@app.get('/')
def hello_api():
	return {"detail":"hello World"}
