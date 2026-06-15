# FILM-MANAGEMENT-SYSTEM
## A simple API server to manage films
#### Memory only
- No database
- No file
---
## File Structure
```
film_management_system/
├── data.py
├── main.py
├── routers/
│    └── movies.py
│    
├── README.md
└── requirements.txt
```

- `main.py` - where tha application runs
- `data.py` - contains a simple python list
- `routers/movies.py` - the routes for main
---
## Data Structure
```
[
    {
   "id": 1,
   "title": "Inception",
   "year": 2010,
   "genre": "Sci-Fi",
   "available": true
    },
    {
   "id": 2,
   "title": "Harry Potter",
   "year": 2002,
   "genre": "Fiction",
   "available": true
    }
     
]
```
---
## Rules


---

## Endpoints


| Method | Endpoint | description |
| :--- | :--- | :--- |
| GET | /movies | all movies |
| GET | /movies/{id} | movie by ID |
| POST | /movies | creating a movie |
| DELETE | /movies/{id} | delete a movie |
| PUT | /movies/{movie_id} | update a movie |
| PATCH | /movies/{movie_id}/availability | change availability |
| GET | /movies/search/genre | movie by genre |
| GET | /movies/search/year | movie by year |
| GET | /movies/count | movies count |
| DELETE | /movies | delete all movies |

