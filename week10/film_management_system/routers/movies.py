from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import data

router = APIRouter()

class NewMovie(BaseModel):
    title: str
    year: int
    genre: str

def create_id() -> int:
    last_id = data.movies[-1]["id"]
    return last_id + 1


@router.get("")
def all_movies():
    return data.movies


@router.get("/{movie_id}")
def movie_by_id(movie_id : int) -> dict:
    movies = data.movies
    ret_val = [m for m in movies if m["id"] == movie_id][0]
    return ret_val

@router.post("", status_code=201)
def add_movie(body: NewMovie):
    new_id = create_id()
    new_movie = {
        "id": new_id,
        "title": body.title,
        "year": body.year,
        "genre": body.genre,
        "available": True
    }
    data.movies.append(new_movie)
    return {
           "status": "success",
           "new id": new_id
            }


@router.delete("/{movie_id}")
def delete_movie(movie_id: int):
    return {"status": "success"}


@router.put("/{movie_id}")
def update_name(movie_id: int, new_name: str):
    return {"status": "success"}


@router.patch("/{movie_id}/availability")
def set_availability(movie_id):
    return {"status": "success"}


@router.get("/search/genre")
def search_by_genre(genre: str):
    return {}



@router.get("/search/year")
def search_by_year(year: int):
    return {}

@router.get("/count")
def search_by_year():
    return {"count_movies": 0}


@router.delete("")
def delete_all_movie():
    return {"status": "success"}