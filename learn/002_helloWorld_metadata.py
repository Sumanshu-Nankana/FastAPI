from fastapi import FastAPI


# we can pass the metadata information for API
# some fields are of type string and some are of type dictionary (example - contact)
# https://fastapi.tiangolo.com/tutorial/metadata/
# title = title of the API
# version = version of the API. This is the version of your application, not of OpenAPI
# we can see all this metadata information on /docs path of application
# http://localhost:8000/docs

description = """
Hello World API
## Heading
**Return JSON format of Hello World **
"""

app = FastAPI(
    title="JobBoard",
    version="0.0.1",
    description=description,
    contact={"name": "Sumanshu Nankana", "email": "sumanshunankana@gmail.com"},
)


@app.get("/")
def hello_api():
    return {"detail": "hello World"}
