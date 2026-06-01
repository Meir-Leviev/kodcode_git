from fastapi import FastAPI

app = FastAPI()


@app.get("/calc/{a}/{op}/{b}")
def calc(a: int, op: str, b: int):
    if op == "add":
        result = a + b
    elif op == "sub":
        result = a - b
    elif op == "mul":
        result = a * b
    elif op == "div":
        if b == 0:
            return {"error": "Division by zero is not allowed"}
        result = a / b
    else:
        return {"error": f"Invalid operation '{op}'. Choose from add, sub, mul, div."}
    return {"operation": op, "result": result}
