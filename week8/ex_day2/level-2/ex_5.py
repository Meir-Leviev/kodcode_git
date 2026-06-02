from fastapi import FastAPI
import json

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
    

app = FastAPI()

@app.get("/todos")
def get_data():
    return load_json("example.json")

@app.post("/todos")
def add_todo():
    def add_todo(data):
        pass

