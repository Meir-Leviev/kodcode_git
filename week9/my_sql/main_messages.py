from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal
import db_messages as db_m

app = FastAPI()


class NewMessage(BaseModel):
    unit: str
    classification: Literal["unclassified", "confidential", "secret", "top_secret"]
    content: str
    source: str


class UpdateMessage(BaseModel):
    unit: str | None = None
    classification: (
        Literal["unclassified", "confidential", "secret", "top_secret"] | None
    ) = None
    content: str | None = None
    source: str | None = None


@app.post("/setup", status_code=201)
def run_setup():
    # In real code this would call setup logic
    # For now just confirm
    return {"status": "ok", "table": "intel_messages"}


@app.get("/schema")
def get_schema():
    columns = db_m.get_schema()
    return {"columns": columns}


@app.get("/messages")
def get_all_message():
    return {"messages": db_m.get_all_messages()}


@app.post("/messages", status_code=201)
def add_new(data: NewMessage):
    new_id = db_m.create_message(
        data.unit, data.classification, data.content, data.source
    )
    return {"created": f"message_id {new_id}"}


@app.get("/messages/{message_id}")
def get_by_id(message_id: int):
    ret_val = db_m.get_message_by_id(message_id)
    if ret_val is None:
        raise HTTPException()
    return ret_val


@app.put("/messages/{message_id}")
def edit_message(message_id: int, body: UpdateMessage):
    data = body.model_dump(exclude_none=True)
    success = db_m.update_messages(message_id, data)
    if not success:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"message": "Updated"}


@app.delete("/messages/{message_id}")
def remove_message(message_id: int):
    success = db_m.delete(message_id)
    if not success:
        raise HTTPException(status_code=404, detail="Message not found")
    return {"message": "Deleted"}
