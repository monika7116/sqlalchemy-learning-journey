from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import datetime

DATABASE_URL = "sqlite:///employee_payroll.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)


# -------------------------------
# MODELS
# -------------------------------

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    department = Column(String)
    designation = Column(String)
    salary = Column(Float)
    joining_date = Column(Date, default=datetime.date.today)

    attendance = relationship("Attendance", back_populates="employee")
    payslips = relationship("Payslip", back_populates="employee")


class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    date = Column(Date, default=datetime.date.today)
    status = Column(String)  # Present / Absent

    employee = relationship("Employee", back_populates="attendance")


class Payslip(Base):
    __tablename__ = 'payslip'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'))
    month = Column(String)  # e.g., 'July 2025'
    basic_salary = Column(Float)
    total_present = Column(Integer)
    net_pay = Column(Float)

    employee = relationship("Employee", back_populates="payslips")


# Base.metadata.create_all(bind=engine)  # Uncomment only once


# -------------------------------
# JOINS
# -------------------------------
session = SessionLocal()

#  INNER JOIN: Employee with Attendance
print("\n--- INNER JOIN: Employee with Attendance ---")
results = session.query(Employee.name, Attendance.date, Attendance.status).join(Attendance).all()
for row in results:
    print(row)

#  LEFT OUTER JOIN: Get all Employees, even those without Attendance
print("\n--- LEFT OUTER JOIN: Employee with Attendance ---")
results = session.query(Employee.name, Attendance.date, Attendance.status).outerjoin(Attendance).all()
for row in results:
    print(row)

#  JOIN with Payslip Info
print("\n--- Employee Payslip Details ---")
results = session.query(Employee.name, Payslip.month, Payslip.net_pay).join(Payslip).all()
for row in results:
    print(row)

session.close()
