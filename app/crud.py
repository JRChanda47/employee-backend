"""
CRUD operations for Employee Management System
"""
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from . import models
from . import schemas

def create_employee(db: Session, employee: schemas.EmployeeCreate):
    """
    Create a new employee in the database
    """
    try:
        db_employee = models.Employee(
            name=employee.name,
            email=employee.email,
            department=employee.department,
            salary=employee.salary
        )
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

def get_employees(db: Session, skip: int = 0, limit: int = 100):
    """
    Get all employees with pagination
    """
    return db.query(models.Employee).offset(skip).limit(limit).all()

def get_employee(db: Session, employee_id: int):
    """
    Get a specific employee by ID
    """
    employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    return employee

def update_employee(db: Session, employee_id: int, employee: schemas.EmployeeUpdate):
    """
    Update an existing employee
    """
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    
    # Update only provided fields
    # update_data = employee.model_dump(exclude_unset=True)
    update_data = employee.model_dump(mode="dict", exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_employee, field, value)
    
    try:
        db.commit()
        db.refresh(db_employee)
        return db_employee
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists"
        )

def delete_employee(db: Session, employee_id: int):
    """
    Delete an employee by ID
    """
    db_employee = db.query(models.Employee).filter(models.Employee.id == employee_id).first()
    if not db_employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found"
        )
    
    db.delete(db_employee)
    db.commit()
    return {"message": "Employee deleted successfully"}
