from fastapi import APIRouter
from database import SessionLocal
from models import Product

router = APIRouter()

# 📦 Get all inventory
@router.get("/inventory")
def get_inventory():
    db = SessionLocal()
    items = db.query(Product).all()
    return items


# ➕ Add new product (with expiry)
@router.post("/inventory/add")
def add_product(name: str, stock: int, expiry: str):
    db = SessionLocal()
    product = Product(name=name, stock=stock, expiry=expiry)
    db.add(product)
    db.commit()
    return {"message": "Product added successfully"}


# ⚠️ Low stock alert
@router.get("/inventory/low")
def low_stock():
    db = SessionLocal()
    items = db.query(Product).all()
    return [item for item in items if item.stock < 20]


# ⏳ Expiry risk (very important feature)
@router.get("/inventory/expiry")
def expiry_risk():
    db = SessionLocal()
    items = db.query(Product).all()
    return [item for item in items if item.expiry < "2026-06"]