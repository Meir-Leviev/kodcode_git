from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import db
import queries as q

app = FastAPI()


class SoldierIn(BaseModel):
    name: str | None = None
    rank: str | None = None
    unit: str | None = None


@app.post("/setup", status_code=201)
def run_setup():
    # In real code this would call setup logic
    # For now just confirm
    return {"status": "setup triggered"}


@app.get("/schema")
def get_schema():
    columns = db.get_schema()
    return {"columns": columns}


@app.get("/soldiers")
def list_soldiers(
    rank: str | None = Query(default=None),
    sort: str | None = Query(default=None),
    unit: str | None = Query(default=None),
    active: bool | None = Query(default=None)
):
    if (rank, sort, unit, active) == (None, None, None, None):
        return {"soldiers": db.get_all()}
    if rank:
        func = q.get_by_rank(rank)
    if sort:
        func = q.get_active_sorted(sort)
    if unit:
        func = q.get_by_unit(unit)
    if active is not None:
        func = q.get_active_sorted(active)
    return {"soldiers": func}
    

@app.get("/soldiers/missing-rank")
def missing_rank():
    return {"soldiers": q.get_missing_rank()}


@app.get("/soldiers/units")
def list_units():
    return {"units": q.get_distinct_units()}


@app.get("/soldiers/search")
def search_soldiers(
    name: str | None = Query(default=None),
    unit: str | None = Query(default=None),):
    return {"soldiers": q.search_by_name(name)}


@app.post("/soldiers", status_code=201)
def add_soldier(body: SoldierIn):
    new_id = db.create(body.name, body.rank, body.unit)
    return {"id": new_id, "message": "Soldier created"}


@app.get("/soldiers/{soldier_id}")
def get_soldier(soldier_id: int):
    soldier = db.get_by_id(soldier_id)
    if soldier is None:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return soldier


@app.put("/soldiers/{soldier_id}")
def edit_soldier(soldier_id: int, body: SoldierIn):
    data = body.model_dump(exclude_none=True)
    success = db.update(soldier_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Updated"}


@app.delete("/soldiers/{soldier_id}")
def remove_soldier(soldier_id: int):
    success = db.delete(soldier_id)
    if not success:
        raise HTTPException(status_code=404, detail="Soldier not found")
    return {"message": "Deleted"}
