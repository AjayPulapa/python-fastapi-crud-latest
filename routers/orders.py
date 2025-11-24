"""
routers/orders.py
------------------
Routes for Orders CRUD using RAW SQL.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud_orders as order_crud
from schemas import OrderCreate, OrderOut
from typing import List

router = APIRouter(
    prefix="/orders",
    tags=["Orders (Raw SQL)"]
)


@router.post("", response_model=OrderOut)
def create_order(data: OrderCreate, db: Session = Depends(get_db)):
    return order_crud.create_order(db, data)


@router.get("", response_model=List[OrderOut])
def get_orders(db: Session = Depends(get_db)):
    return order_crud.get_all_orders(db)


@router.get("/{order_id}", response_model=OrderOut)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = order_crud.get_order(db, order_id)
    if not order:
        raise HTTPException(404, "Order not found")
    return order


@router.put("/{order_id}", response_model=OrderOut)
def update_order(order_id: int, data: OrderCreate, db: Session = Depends(get_db)):
    updated = order_crud.update_order(db, order_id, data)
    if not updated:
        raise HTTPException(404, "Order not found")
    return updated


@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(get_db)):
    order_crud.delete_order(db, order_id)
    return {"message": "Order deleted successfully"}
