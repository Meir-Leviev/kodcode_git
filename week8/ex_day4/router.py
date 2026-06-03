from fastapi import APIRouter, HTTPException

router = APIRouter()


# 1
@router.get("/numbers/{n}")
def positive_num(n: int):
    try:
        if n < 0:
            raise HTTPException(status_code=404, detail="Number must be positive")
        return {
            "value": n
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"server crash {e}")
    

# 2
students = {"101": "Moshe", "102": "Yosef"}

@router.get("/students/{student_id}")
def get_by_id(student_id: str):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students.get(student_id)



# 3
@router.post("/students/{student_id}")
def add_student(student_id, body: dict):
    if student_id in students:
        raise HTTPException(status_code=409, detail="student_id is already taken")
    if body.get("name") == None:
        raise HTTPException(status_code=400, detail="No ['name'] field")
    students[student_id] = body["name"]
    return body