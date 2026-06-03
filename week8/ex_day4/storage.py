from fastapi import HTTPException
import json


def load_data() -> dict:
    try:
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileExistsError, FileNotFoundError:
        return {}


def save_data(data: dict) -> None:
    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception:
        raise HTTPException(status_code=500, detail="Storage error")
