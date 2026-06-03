from fastapi import FastAPI, HTTPException
import uvicorn
from shape_manager import ShapeManager
from main import create_id


def find_shape(id):
    shapes = manager.get_all_shapes()
    for s in shapes:
        if s.get("id") == id:
            return shapes
    return None




app = FastAPI()

manager = ShapeManager()


@app.get("/shapes")
def get_all():
    shapes = manager.get_all_shapes()
    return shapes


@app.get("/shapes/total-area")
def total_area():
    shapes = manager.get_all_shapes()
    total = sum(s["area"] for s in shapes)
    return {
        "total_area": total
    }


@app.get("/shapes/count")
def count_shapes():
    shapes = manager.get_all_shapes()
    cnt = len(shapes)
    return {
        "shapes_count": cnt
    }

@app.get("/shapes/{id}")
def get_shape(id: int):
    shape = find_shape(id)
    if shape:
        return shape
    raise HTTPException(404, "not found")

@app.post("/shapes", status_code=201)
def create_shape(body: dict):
    new_id = create_id(manager)
    body["id"] = new_id
    manager.create_shape(body)
    manager.save_to_json()
    return {
        "status": "new shape added",
        "new_id": new_id
    }
    

@app.put("/shapes/{id}")
def replace_shape(id: int, body: dict):
    shape = find_shape(id)
    if shape:
        body["id"] = id
        manager.update_shape(id, body)
        manager.save_to_json()
        return {
            "status": "success"
        }
    raise HTTPException(404)

@app.delete("/shapes/{id}")
def delete_shape(id: int):
    shape = find_shape(id)
    if shape:
        manager.delete_shape(id)
        manager.save_to_json()
        return {
            "status": "success"
        }
    raise HTTPException(404)


@app.get("/shapes/type/{type}")
def by_type(type: str):
    shapes = manager.get_all_shapes()
    by_type = [s for s in shapes if s["type"].lower() == type.lower()]
    return by_type


if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8000, reload=True)
