from fastapi import APIRouter

router = APIRouter()

@router.get("/ai/recommend")
def recommend():
    return {
        "suggestion": "Increase stock of Paracetamol (high demand)"
    }