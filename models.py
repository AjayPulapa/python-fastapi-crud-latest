"""
models.py
---------
SQLAlchemy ORM models for auto-creating tables.
Employees uses ORM CRUD.
Orders uses RAW SQL CRUD, but still mapped so tables auto-create.
"""

from sqlalchemy import Column, Integer, String
from database import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    department = Column(String(100))


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product = Column(String(100))
    amount = Column(Integer)


Base.metadata.create_all(bind=engine)
