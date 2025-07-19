 1. What is a One-to-Many Relationship?
A One-to-Many relationship means:

One row in Table A → can be related to many rows in Table B

Example in your payroll system:

One Department has many Employees

One Employee can have many Attendance records

🔸 2. Declaring One-to-Many Relationship in SQLAlchemy
Step-by-step:
A. Define the "One" side
python
Copy
Edit
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    employees = relationship("Employee", back_populates="department")
B. Define the "Many" side
python
Copy
Edit
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship("Department", back_populates="employees")
🔁 relationship() and ForeignKey() connect both sides.

🔹 3. Real-World Example from Your Project
One Employee → Many Attendance Records

python
Copy
Edit
class Attendance(Base):
    __tablename__ = 'attendances'

    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)

    employee_id = Column(Integer, ForeignKey('employees.id'))
    employee = relationship("Employee", back_populates="attendances")
python
Copy
Edit
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    attendances = relationship("Attendance", back_populates="employee")
✅ 4. Creating Data with One-to-Many
Add Department and Employees:
python
Copy
Edit
dept = Department(name="HR")
emp1 = Employee(name="Monika", department=dept)
emp2 = Employee(name="Raj", department=dept)

session.add_all([dept, emp1, emp2])
session.commit()
🔍 5. Querying One-to-Many Relationships
A. Get all employees of a department:
python
Copy
Edit
dept = session.query(Department).filter_by(name="HR").first()
for emp in dept.employees:
    print(emp.name)
B. Get department of an employee:
python
Copy
Edit
emp = session.query(Employee).first()
print(emp.department.name)
🔧 6. Use in Your Payroll Project
Use Case	Table A → Table B
One Department → Many Employees	Department → Employee
One Employee → Many Attendances	Employee → Attendance
One Employee → Many Salaries	Employee → Payroll (if per month)



