import json
from logging_config import logger


def load_file() -> list | list[dict]:
    """
    Returns the full content of weapons.json
    if file not found returns []
    """
    try:
        with open("weapons.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        logger.debug("File founded returning content")
        return data
    except FileNotFoundError as e:
        logger.exception(f"{e}")
        logger.debug("returning []")
        return []


def create_id() -> int:
    """
    Before saving to the file you need to have an ID
    this func reads the file and takes the last ID number
    returning last ID + 1
    """
    new_id = 1
    weapons = load_file()
    if not weapons:
        logger.debug("nothing in weapons returning 1")
        return new_id
    max_id = max(weapons, key=lambda w: w["id"])
    max_id = max_id.get("id")
    new_id = max_id + new_id  
    logger.debug(f"Returning new ID: {new_id}")
    return new_id


def save_file(data):
    """
    saving the data into weapons.json
    """
    with open("weapons.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        logger.debug("file saved")
