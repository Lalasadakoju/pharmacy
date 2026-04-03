from fastapi import FastAPI
from database import engine
from models import Base
import auth, inventory, billing, ai

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(inventory.router)
app.include_router(billing.router)
app.include_router(ai.router)

@app.get("/")
def home():
    return {"message": "Pharmacy API Running"}