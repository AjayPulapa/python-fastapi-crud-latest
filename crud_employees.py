"""
crud_employees.py
------------------
Employee CRUD using SQLAlchemy ORM.
"""

from sqlalchemy.orm import Session
from models import Employee
from schemas import EmployeeCreate


def create_employee(db: Session, data: EmployeeCreate):
    emp = Employee(name=data.name, department=data.department)
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp


def get_all_employees(db: Session):
    return db.query(Employee).all()


def get_employee(db: Session, emp_id: int):
    return db.query(Employee).filter(Employee.id == emp_id).first()


def update_employee(db: Session, emp_id: int, data: EmployeeCreate):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if emp:
        emp.name = data.name
        emp.department = data.department
        db.commit()
        db.refresh(emp)
    return emp


def delete_employee(db: Session, emp_id: int):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if emp:
        db.delete(emp)
        db.commit()
    return emp
