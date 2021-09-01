from fastapi import FastAPI


# By default, the OpenAPI schema is served at /openapi.json
# But you can configure it with the parameter openapi_url
app = FastAPI(openapi_url="/api/v1/openapi.json")


# we can use our own tags using 'tags' parameter
@app.get("/users", tags=["users"])
def hello_api():
    return {"detail": "hello user"}


# we can use our own tags using 'tags' parameter
@app.get("/items", tags=["items"])
def hello_api():
    return {"detail": "hello item"}
