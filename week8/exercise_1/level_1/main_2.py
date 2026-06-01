from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"service": "my-api", "version": "1.0"}

@app.get("/users/admin")
def get_admin():
    return {
        "role": "admin",
        "access": "full"
    }

@app.get("/users/{user_id}")
def get_info(user_id):
    return {
            "user_id": user_id,
            "name": "john doe",
            "email": "user@email.com"
            }



