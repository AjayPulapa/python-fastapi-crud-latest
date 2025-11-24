"""
crud_orders.py
---------------
Orders CRUD using RAW SQL queries.
"""

from sqlalchemy.orm import Session
from schemas import OrderCreate


def create_order(db: Session, data: OrderCreate):
    query = "INSERT INTO orders (product, amount) VALUES (:product, :amount)"
    db.execute(query, {"product": data.product, "amount": data.amount})
    db.commit()

    last_id = db.execute("SELECT LAST_INSERT_ID()").scalar()

    return {"id": last_id, "product": data.product, "amount": data.amount}


def get_all_orders(db: Session):
    rows = db.execute("SELECT * FROM orders").fetchall()
    return [dict(row) for row in rows]


def get_order(db: Session, order_id: int):
    row = db.execute("SELECT * FROM orders WHERE id = :id", {"id": order_id}).fetchone()
    return dict(row) if row else None


def update_order(db: Session, order_id: int, data: OrderCreate):
    query = """
        UPDATE orders
        SET product = :product, amount = :amount
        WHERE id = :id
    """
    db.execute(query, {"product": data.product, "amount": data.amount, "id": order_id})
    db.commit()

    return get_order(db, order_id)


def delete_order(db: Session, order_id: int):
    db.execute("DELETE FROM orders WHERE id = :id", {"id": order_id})
    db.commit()
    return {"message": "Order deleted"}
