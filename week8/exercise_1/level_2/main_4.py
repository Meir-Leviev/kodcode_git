from fastapi import FastAPI
from datetime import datetime


app = FastAPI()

@app.get("/status")
def get_status():
    return {
        "server_name": "my_server",
        "current_time": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }