from fastapi import APIRouter
from database import SessionLocal
from models import Product, Sale

router = APIRouter()

@router.post("/billing")
def create_bill(product_id: int, quantity: int):
    db = SessionLocal()

    product = db.query(Product).filter(Product.id == product_id).first()

    if not product:
        return {"error": "Product not found"}

    if product.stock < quantity:
        return {"error": "Not enough stock"}

    # reduce stock
    product.stock -= quantity

    # create sale record
    sale = Sale(product_id=product_id, quantity=quantity)
    db.add(sale)

    db.commit()

    return {"message": "Bill created successfully"}