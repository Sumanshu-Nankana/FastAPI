from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_api():
    return {"detail": "hello World"}
