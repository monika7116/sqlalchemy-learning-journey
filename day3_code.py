from sqlalchemy import create_engine, Column, Integer, String, Float, Date 
from sqlalchemy.orm import declarative_base, sessionmaker 
import datetime 

# Step 1: Setup
DATABASE_URL = "sqlite:///employee_payroll.db" 
engine = create_engine(DATABASE_URL, echo=False) 
Base = declarative_base() 
SessionLocal = sessionmaker(bind=engine) 

# Step 2:Employee Model 
class Employee(Base):
    __tablename__= 'employees' 

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    department = Column(String(50))
    designation = Column(String(50))
    salary = Column(Float)
    joining_date = Column(Date, default=datetime.date.today) 

# step 3: Open a session
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Step 4: Insert multiple employees 
employees = [
    Employee(name= "Sita Sharma", email="sita@ex.com", department="Finance", designation="Analyst", salary=55000, joining_date=datetime.date(2023, 4, 10)), 
    Employee(name= "Amit Joshi", email="amit@ex.com", department="IT", designation="Developer", salary=65000, joining_date=datetime.date(2022, 5, 11)) ,
    Employee(name= "Meena Verma", email="meena@ex.com", department="HR", designation="Executive", salary=48000, joining_date=datetime.date(2023, 4, 9)) 

]

session.add_all(employees)
session.commit()
session.close()

# Step 5: Read all employees
print("\n All Employees:")
all_employees = session.query(Employee).all()
for emp in all_employees:
    print(f"{emp.id}. {emp.name} ({emp.email}) - {emp.department}, ₹{emp.salary}")


# Step 6: Filter by department
print("\n IT Department Employees:")
it_emps = session.query(Employee).filter(Employee.department == "IT").all()
for emp in it_emps:
    print(f"{emp.name} - {emp.designation}")

# Step 7: Filter by salary
print("\n Employee with Salary > 50000:")
high_salary_emps = session.query(Employee).filter(Employee.salary > 50000).all()
for emp in high_salary_emps:
    print(f"{emp.name} - ₹{emp.salary}")

session.close()
