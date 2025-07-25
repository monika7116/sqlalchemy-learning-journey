from sqlalchemy import create_engine, func, extract
from sqlalchemy.orm import sessionmaker
from models import Base, Employee, Attendance
from datetime import date

engine = create_engine('sqlite:///epms.db')
Session = sessionmaker(bind=engine)
session = Session()

month = 7
year = 2025

employees = session.query(Employee).all()

for emp in employees:
    present = session.query(func.count(Attendance.id)).filter(
        Attendance.employee_id == emp.id,
        Attendance.is_present == True,
        extract('month', Attendance.date) == month,
        extract('year', Attendance.date) == year
    ).scalar()

    absent = session.query(func.count(Attendance.id)).filter(
        Attendance.employee_id == emp.id,
        Attendance.is_present == False,
        extract('month', Attendance.date) == month,
        extract('year', Attendance.date) == year
    ).scalar()

    print(f"{emp.name}: Present = {present} days, Absent = {absent} days")
