from fastapi import FastAPI


# we can create a tags for different routes
# Create metadata for your tags and pass it to the openapi_tags parameter
tags_metadata = [
    {"name": "users", "description": "All the operations related with users."},
    {"name": "items", "desciption": "All the operations related with items."},
]

description = """
Hello World API
## Heading
**Return JSON format of Hello World **
"""

app = FastAPI(
    title="JobBoard",
    version="0.0.1",
    description=description,
    contact={"name": "Sumanshu Nankana", "email": "sumanshunankana@gmail.com",},
    openapi_tags=tags_metadata,
)


# we can use our own tags using 'tags' parameter
@app.get("/users", tags=["users"])
def hello_api():
    return {"detail": "hello user"}


# we can use our own tags using 'tags' parameter
@app.get("/items", tags=["items"])
def hello_api():
    return {"detail": "hello item"}
