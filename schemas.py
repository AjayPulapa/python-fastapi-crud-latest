"""
schemas.py
-----------
Pydantic schemas for request and response validation.
"""

from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    department: str


class EmployeeOut(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True


class OrderCreate(BaseModel):
    product: str
    amount: int


class OrderOut(OrderCreate):
    id: int

    class Config:
        from_attributes  = True
