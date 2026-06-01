from fastapi import FastAPI

app = FastAPI()


@app.get('/ping')
def ping_pong():
    return {"status": "pong"}


@app.get("/greet/{name}")
def greet(name):
    return {"message": f"Hello, {name}!"}
