"""
main.py
--------
Main application that registers all routers.
"""

from fastapi import FastAPI
from routers import employees, orders

app = FastAPI(title="FastAPI + MySQL (ORM + Raw SQL)")

app.include_router(employees.router)
app.include_router(orders.router)
