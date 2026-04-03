# Pharmacy Store Operations Platform

## Overview
This project is a mobile-first backend system for managing pharmacy store operations across multiple outlets. It is built using FastAPI and SQLite.

## Features
- Secure API-based architecture
- Inventory management with stock tracking
- Billing system with automatic stock reduction
- Expiry tracking for medicines
- Low stock alerts
- AI-based recommendation endpoint

## Tech Stack
- Python (FastAPI)
- SQLite (Database)
- SQLAlchemy (ORM)

## APIs
- /inventory → View products
- /inventory/add → Add product
- /inventory/low → Low stock alert
- /inventory/expiry → Expiry risk detection
- /billing → Create bill and reduce stock
- /ai/recommend → AI suggestions

## How to Run
1. Activate virtual environment
2. Install dependencies:
   pip install fastapi uvicorn sqlalchemy
3. Run server:
   python -m uvicorn main:app
4. Open:
   http://127.0.0.1:8000/docs

## Future Enhancements
- Role-based authentication
- Cloud deployment
- Advanced AI forecasting
