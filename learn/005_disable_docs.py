from fastapi import FastAPI

# If you want to disable the OpenAPI schema completely you can set openapi_url=None,
# that will also disable the documentation user interfaces that use it.

app = FastAPI(openapi_url=None)


# we can use our own tags using 'tags' parameter
@app.get("/users", tags=["users"])
def hello_api():
    return {"detail": "hello user"}


# we can use our own tags using 'tags' parameter
@app.get("/items", tags=["items"])
def hello_api():
    return {"detail": "hello item"}
