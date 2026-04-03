from sqlalchemy import Column, Integer, String
from database import Base

# 📦 Product table
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    stock = Column(Integer)
    expiry = Column(String)


# 🧾 Sales table
class Sale(Base):
    __tablename__ = "sales"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    quantity = Column(Integer)