"""
routers/employees.py
---------------------
Routes for Employee CRUD using ORM.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud_employees as emp_crud
from schemas import EmployeeCreate, EmployeeOut
from typing import List

router = APIRouter(
    prefix="/employees",
    tags=["Employees (ORM)"]
)


@router.post("", response_model=EmployeeOut)
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    return emp_crud.create_employee(db, data)


@router.get("", response_model=List[EmployeeOut])
def get_employees(db: Session = Depends(get_db)):
    return emp_crud.get_all_employees(db)


@router.get("/{emp_id}", response_model=EmployeeOut)
def get_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = emp_crud.get_employee(db, emp_id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    return emp


@router.put("/{emp_id}", response_model=EmployeeOut)
def update_employee(emp_id: int, data: EmployeeCreate, db: Session = Depends(get_db)):
    emp = emp_crud.update_employee(db, emp_id, data)
    if not emp:
        raise HTTPException(404, "Employee not found")
    return emp


@router.delete("/{emp_id}")
def delete_employee(emp_id: int, db: Session = Depends(get_db)):
    emp = emp_crud.delete_employee(db, emp_id)
    if not emp:
        raise HTTPException(404, "Employee not found")
    return {"message": "Employee deleted successfully"}
