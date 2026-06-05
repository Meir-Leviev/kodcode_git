from fastapi import FastAPI
import uvicorn
from logging_config import logger
from routes import notes

app = FastAPI()

app.include_router(notes.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
