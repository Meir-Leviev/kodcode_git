from fastapi import FastAPI
import uvicorn
from routers import greet

app = FastAPI()

app.include_router(greet.router)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
