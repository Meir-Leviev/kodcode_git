from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from logging_config import logger
import storage


class NewWeapon(BaseModel):
    type: str
    model: str
    ammo_type: str
    condition: str


app = FastAPI()


@app.get("/weapons")
def get_all_weapons():
    """
    Returns the full content of weapons.json
    if the file does not exist yet load_file() will return []
    """
    logger.debug("Request received")
    weapons = storage.load_file()
    logger.debug("returning weapons")
    return weapons


@app.get("/weapons/by-condition")
def get_by_condition(condition):
    """
    Return all weapons with the given condition
    if not found - 404

    """
    logger.debug("Request received")
    weapons = storage.load_file()
    conditions = [w["condition"] for w in weapons]
    if condition.lower() not in conditions:
        raise HTTPException(status_code=404)
    ret_val = [w for w in weapons if w["condition"] == condition]
    logger.debug("Sending ret_val to client")
    return ret_val

@app.delete("/weapons/by-condition")
def delete_by_condition(condition):
    """
    Delete all weapons with given condition
    """
    logger.debug("Request received")
    weapons = storage.load_file()
    weapons_copy = weapons.copy()
    for w in weapons_copy:
        if w["condition"] == condition.lower():
            weapons.remove(w)
    logger.debug("finished deleting saving file")
    storage.save_file(weapons)
    return

@app.get("/weapons/combat-ready") # Unfortunately I added "/combat-ready" only after the test
def get_by_type(type):
    """
    Return all weapons with the given type
    if not found - 404
    """
    logger.debug("Request received")
    weapons = storage.load_file()
    weapons_type = [w for w in weapons if w["type"] == type]
    conditions = ["new", "good"]
    ret_val = [w for w in weapons_type if w["condition"] in conditions]
    if not ret_val:
        logger.debug("type not found rasing 404")
        raise HTTPException(status_code=404, detail="type not found")
    logger.debug("Sending ret_val to client")
    return ret_val


@app.get("/weapons/summary/by-type")
def summary():
    """
    Returns a summary of weapons
    """
    logger.debug("Request received")
    weapons = storage.load_file()
    ret_val = {}
    for w in weapons:
        ret_val[w["type"]] = ret_val.get(w["type"], 0) + 1
    return ret_val


@app.get("/weapons/{id}")
def get_by_id(id: int):
    """
    Returns a weapon by its ID
    if not found raising 404
    """
    logger.debug("Request received")
    weapons = storage.load_file()
    try:
        for w in weapons:
            if w.get("id") == id:
                logger.debug("weapon found returning to client")
                return w
        logger.debug("ID not found; raising 404")
        raise HTTPException(status_code=404, detail="ID not found")
    except Exception as e:
        logger.exception(f"{e}")
        raise


@app.post("/weapons", status_code=201)
def add_weapon(body: NewWeapon):
    """
    Adds new weapon from body
    if body json data not as the class NewWeapon it will send 422
    """
    logger.debug("POST request received")

    weapons = storage.load_file()
    new_id = storage.create_id()
    body_dict = body.model_dump()
    body_dict["id"] = new_id
    weapons.append(body_dict)
    logger.debug("Saving new weapon to file")
    storage.save_file(weapons)
    return {"status": "new weapon saved"}


@app.put("/weapons/{id}")
def update_weapon(id: int, body: dict):
    """
    Expecting a json as class UpdateWeapon and ID in params
    will find the ID and change the weapon
    """
    logger.debug("PUT request received")
    weapons = storage.load_file()
    try:
        for i, w in enumerate(weapons):
            if w.get("id") == id:
                logger.debug("weapon found")
                body["id"] = w["id"]
                w.update(body)
                del weapons[i]
                weapons.append(w)
                logger.debug("Weapon updated saving to file")
                storage.save_file(weapons)
                return
        logger.debug("ID not found; raising 404")
        raise HTTPException(status_code=404, detail="ID not found")
    except Exception as e:
        logger.exception(f"{e}")
        raise


@app.delete("/weapons/{id}")
def delete_weapon(id: int):
    """
    Delete a weapon by its ID
    if not found raising 404
    """
    logger.debug("Request received")
    weapons = storage.load_file()
    try:
        for i, w in enumerate(weapons):
            if w.get("id") == id:
                logger.debug("weapon found")
                del weapons[i]
                logger.debug("Weapon deleted. updating file")
                storage.save_file(weapons)
                return
        logger.debug("ID not found; raising 404")
        raise HTTPException(status_code=404, detail="ID not found")
    except Exception as e:
        logger.exception(f"{e}")
        raise
