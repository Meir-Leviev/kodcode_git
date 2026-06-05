from fastapi import APIRouter , HTTPException
from pydantic import BaseModel
from storage import utils
from logging_config import logger

FILE_NAME = "notes.json"

class Note(BaseModel):
    id: str
    text: str



router = APIRouter()


@router.get("/notes")
def all_notes():
    logger.debug("loading file")
    notes = utils.load_file(FILE_NAME)
    logger.debug("finish loading file")
    logger.debug("Sending all notes")
    return notes

@router.get("/notes/{id}")
def get_note(id: str):
    logger.debug("loading file")
    notes = utils.load_file(FILE_NAME)
    logger.debug("finish loading file")
    try:
        for n in notes:
            if id == n.get("id"):
                logger.debug("note found returning to client")
                return n
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        logger.exception(f"{e}")
        raise


@router.post("/notes/{id}")
def add_note(id: str, body: Note):
    body.id = id
    logger.debug(f"loading file ")
    notes = utils.load_file(FILE_NAME)
    logger.debug("finish loading file")
    body_dict = body.model_dump_json()
    if notes == []:
        utils.save_file(FILE_NAME, [body_dict])
        logger.info("File saved")
        return {"status": "note saved"}
    try:
        for n in notes:
            if id == n.get("id"):
                raise HTTPException(status_code=409, detail="ID exist")
        if not body.text:
            raise HTTPException(status_code=400, detail="no text")
    except Exception as e:
        logger.exception(f"{e}")
        raise
    notes.append(body_dict)
    utils.save_file(FILE_NAME, notes)
    logger.info("File saved")
    return {"status": "note saved"}


@router.put("/notes/{id}")
def change_note(id: str, body: Note):
    logger.debug("loading file")
    notes = utils.load_file(FILE_NAME)
    logger.debug("finish loading file")
    try:
        for i, n in enumerate(notes):
            if id == n.get("id"):
                notes[i]["text"] = body.text
                utils.save_file(FILE_NAME, notes)
                return {"status": "note saved"}
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        logger.exception(f"{e}")
        raise


@router.delete("/notes/{id}")
def delete_note(id: str):
    logger.debug("loading file")
    notes = utils.load_file(FILE_NAME)
    logger.debug("finish loading file")
    try:
        for i, n in enumerate(notes):
            if id == n.get("id"):
                del notes[i]
                utils.save_file(FILE_NAME, notes)
                return {"delete": id}
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        logger.exception(f"{e}")
        raise
