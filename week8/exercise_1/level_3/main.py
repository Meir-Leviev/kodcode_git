from fastapi import FastAPI

app = FastAPI()

grades = {
    "1": {"name": "Moshe", "grade": 88},
    "2": {"name": "Yaakov", "grade": 75},
    "3": {"name": "David", "grade": 92},
}

sorted_student = sorted(grades.values(), key=lambda g: g["grade"], reverse=True)

@app.get("/students")
def get_students():
    return grades



@app.get("/students/top")
def top():
    return sorted_student[0]


@app.get("/students/average")
def get_avg():
    cnt = len(grades)
    acc = sum(s["grade"] for s in grades.values())
    avg = acc / cnt
    return {"class_average": avg}


@app.get("/students/count")
def count():
    return {"students_count": len(grades)}

@app.get("/students/{student_id}")
def get_one(student_id):
    return grades[student_id]
