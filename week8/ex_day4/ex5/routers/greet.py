from fastapi import APIRouter

router = APIRouter()

@router.get("/hello/{name}")
def greet(name: str):
    return {"message": f"hello {name}"}

