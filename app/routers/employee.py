"""
Employee router for CRUD operations
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, crud
from ..database import get_db

# Create router instance
router = APIRouter(
    prefix="/employees",
    tags=["employees"],
    responses={404: {"description": "Not found"}}
)

@router.post("/", response_model=schemas.EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(employee: schemas.EmployeeCreate, db: Session = Depends(get_db)):
    """
    Create a new employee
    
    - **name**: Employee's full name
    - **email**: Employee's unique email address
    - **department**: Employee's department
    - **salary**: Employee's salary
    """
    return crud.create_employee(db=db, employee=employee)

@router.get("/", response_model=List[schemas.EmployeeResponse])
def get_employees(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all employees with pagination
    
    - **skip**: Number of records to skip (default: 0)
    - **limit**: Maximum number of records to return (default: 100)
    """
    return crud.get_employees(db=db, skip=skip, limit=limit)

@router.get("/{employee_id}", response_model=schemas.EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """
    Get a specific employee by ID
    
    - **employee_id**: ID of the employee to retrieve
    """
    return crud.get_employee(db=db, employee_id=employee_id)

@router.put("/{employee_id}", response_model=schemas.EmployeeResponse)
def update_employee(employee_id: int, employee: schemas.EmployeeUpdate, db: Session = Depends(get_db)):
    """
    Update an existing employee
    
    - **employee_id**: ID of the employee to update
    - **name**: Employee's full name (optional)
    - **email**: Employee's email address (optional)
    - **department**: Employee's department (optional)
    - **salary**: Employee's salary (optional)
    """
    return crud.update_employee(db=db, employee_id=employee_id, employee=employee)

@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    """
    Delete an employee by ID
    
    - **employee_id**: ID of the employee to delete
    """
    return crud.delete_employee(db=db, employee_id=employee_id)
