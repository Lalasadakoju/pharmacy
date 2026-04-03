from fastapi import APIRouter

router = APIRouter()

users = {
    "admin": {"password": "123", "role": "admin"},
    "pharma": {"password": "123", "role": "pharmacist"}
}

@router.post("/login")
def login(username: str, password: str):
    if username in users and users[username]["password"] == password:
        return {"message": "Login successful", "role": users[username]["role"]}
    return {"error": "Invalid credentials"}