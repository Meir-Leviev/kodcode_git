# FILM-MANAGEMENT-SYSTEM
## A simple API server to manage films
#### Requests using `curl` or `Postman`
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

---
## System Flow
` client request > server accept > server read/write the list in data.py >  send respond `

---
## How To Run The Server
- Create a virtual environment
```
# windows

python -m venv .venv
./.venv/Scripts/activate
```
```
# macOS/linux

python3 -m venv .venv
source .venv/bin/activate

```
- install requirements
```
pip install -r requirements.txt
```
- Run `python main.py`  to activate the server
```
cd ~/film_management_system
python main.py
```