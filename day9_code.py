from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from day2_create_employee_table import Base, Employee

DATABASE_URL = "sqlite:///employee_payroll.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)

#  1. Add a new employee
def add_employee(name, email, department, designation, salary, joining_date):
    with SessionLocal() as session:
        employee = Employee(
            name=name,
            email=email,
            department=department,
            designation=designation,
            salary=salary,
            joining_date=joining_date
        )
        session.add(employee)
        session.commit()
        print(f"Employee {name} added.")

# 2. Get all employees
def get_all_employees():
    with SessionLocal() as session:
        return session.query(Employee).all()

# 3. Get employee by email
def get_employee_by_email(email):
    with SessionLocal() as session:
        return session.query(Employee).filter(Employee.email == email).first()

#  4. Delete employee by ID
def delete_employee_by_id(emp_id):
    with SessionLocal() as session:
        emp = session.query(Employee).filter(Employee.id == emp_id).first()
        if emp:
            session.delete(emp)
            session.commit()
            print(f"Employee ID {emp_id} deleted.")
        else:
            print("Employee not found.")

#  5. Update salary by ID
def update_salary(emp_id, new_salary):
    with SessionLocal() as session:
        emp = session.query(Employee).filter(Employee.id == emp_id).first()
        if emp:
            emp.salary = new_salary
            session.commit()
            print(f"Salary updated for ID {emp_id}.")
        else:
            print("Employee not found.")


#  Testing the reusable queries
if __name__ == "__main__":
    import datetime

    add_employee("Anjali", "anjali@example.com", "Finance", "Accountant", 45000, datetime.date(2023, 1, 15))
    print(get_all_employees())
    print(get_employee_by_email("anjali@example.com"))
    update_salary(2, 48000)
    delete_employee_by_id(2)
