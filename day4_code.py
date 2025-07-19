# Day 4: One-to-One Relationship – SQLAlchemy ORM

## What is One-to-One?
A relationship where one record in Table A is related to exactly one record in Table B.

## How to Implement:
- Use `ForeignKey(unique=True)` in B table
- Set `uselist=False` in `relationship()`

## Example: Employee ↔ SalaryAccount

```python
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    salary_account = relationship("SalaryAccount", back_populates="employee", uselist=False)

class SalaryAccount(Base):
    __tablename__ = 'salary_accounts'
    id = Column(Integer, primary_key=True)
    account_number = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), unique=True)
    employee = relationship("Employee", back_populates="salary_account")






---

## 💻 Python Code for Day 4 (Complete)

```python
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Employee Table
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # One-to-One with SalaryAccount
    salary_account = relationship("SalaryAccount", back_populates="employee", uselist=False)

# SalaryAccount Table
class SalaryAccount(Base):
    __tablename__ = 'salary_accounts'

    id = Column(Integer, primary_key=True)
    account_number = Column(String, nullable=False)
    employee_id = Column(Integer, ForeignKey('employees.id'), unique=True)

    employee = relationship("Employee", back_populates="salary_account")

# Setup DB
engine = create_engine("sqlite:///day4_employee_salary.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Sample Data
emp1 = Employee(name="Monika Raj")
account1 = SalaryAccount(account_number="SBIN0001234", employee=emp1)

session.add_all([emp1, account1])
session.commit()

# Fetching
employee = session.query(Employee).first()
print(f"Employee: {employee.name}")
print(f"Account No: {employee.salary_account.account_number}")
