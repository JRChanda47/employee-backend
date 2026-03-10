"""
SQLAlchemy models for Employee Management System
"""
from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Employee(Base):
    """
    Employee model representing the employees table
    """
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    department = Column(String(100), nullable=False)
    salary = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Employee(id={self.id}, name='{self.name}', email='{self.email}')>"
