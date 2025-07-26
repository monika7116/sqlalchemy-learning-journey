generate_payslip.py

from sqlalchemy import create_engine, extract, func
from sqlalchemy.orm import sessionmaker
from models import Base, Employee, Attendance, Payslip

# Database setup
engine = create_engine('sqlite:///epms.db')
Session = sessionmaker(bind=engine)
session = Session()

# Configuration
month = 7
year = 2025
per_day_salary = 1000  # You can change this as needed

# Fetch all employees
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

    total_salary = per_day_salary * present

    # Check if payslip already exists for this employee/month/year
    existing = session.query(Payslip).filter_by(
        employee_id=emp.id, month=month, year=year
    ).first()

    if not existing:
        payslip = Payslip(
            employee_id=emp.id,
            month=month,
            year=year,
            base_salary=per_day_salary,
            present_days=present,
            absent_days=absent,
            total_salary=total_salary
        )
        session.add(payslip)

# Commit the session
session.commit()

# Print results
payslips = session.query(Payslip).filter_by(month=month, year=year).all()
for slip in payslips:
    print(f"{slip.employee.name} - {slip.month}/{slip.year} - ₹{slip.total_salary}")



# Macke sure your models.py includes the payslip model like this:

class Payslip(Base):
    __tablename__ = 'payslips'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    month = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    base_salary = Column(Float, nullable=False)
    present_days = Column(Integer)
    absent_days = Column(Integer)
    total_salary = Column(Float)

    employee = relationship("Employee", back_populates="payslips")

# In Employee model:
payslips = relationship("Payslip", back_populates="employee")
