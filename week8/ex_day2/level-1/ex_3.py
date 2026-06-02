from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet(name="world"):
    return {"message": f"Hello, {name}!"}



