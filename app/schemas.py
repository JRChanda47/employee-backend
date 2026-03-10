"""
Pydantic schemas for Employee Management System
"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class EmployeeBase(BaseModel):
    """
    Base schema for Employee with common fields
    """
    name: str
    email: EmailStr
    department: str
    salary: float

class EmployeeCreate(EmployeeBase):
    """
    Schema for creating a new employee
    """
    pass

class EmployeeUpdate(BaseModel):
    """
    Schema for updating an employee (all fields optional)
    """
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    department: Optional[str] = None
    salary: Optional[float] = None

class EmployeeResponse(EmployeeBase):
    """
    Schema for employee response (includes id)
    """
    id: int
    
    class Config:
        # Enable ORM mode to work with SQLAlchemy models
        from_attributes = True
