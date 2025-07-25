🎯 Objective
To learn and implement relationships between database tables using SQLAlchemy ORM for real-world applications like Payroll, Attendance, and Department-Employee mapping.

🔗 1. What is a Relationship in SQLAlchemy?
A relationship in a database represents how two tables are connected.
In SQLAlchemy, we define relationships using:

relationship() → to link ORM classes

ForeignKey() → to define actual DB constraint

🔁 2. Types of Relationships in SQLAlchemy
Type	Example in EPMS	Description
One-to-Many	Department → Employees	One department can have many employees
Many-to-One	Employees → Department	Each employee belongs to one department
One-to-Many	Employee → Attendance Records	One employee can have many attendance entries
Optional: One-to-One	Employee → Payslip (if only one per month)	One employee has one payslip per month

🛠️ 3. Core Functions & Terms
🔸 ForeignKey()
Used inside a Column to create a reference to another table’s primary key.

python

department_id = Column(Integer, ForeignKey('departments.id'))
🔸 relationship()
Used in the class (ORM side) to link objects.

python

department = relationship("Department", back_populates="employees")
🔸 back_populates
It connects both sides of a relationship explicitly.

python

# In Department
employees = relationship("Employee", back_populates="department")

# In Employee
department = relationship("Department", back_populates="employees")
🧱 4. Real Example: Department → Employees
🔷 Department Table
python
Copy
Edit
class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    employees = relationship("Employee", back_populates="department")
🔷 Employee Table
python
Copy
Edit
class Employee(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship("Department", back_populates="employees")
🔗 Relationship Flow:
A department can access its employees via .employees

An employee can access their department via .department

🧱 5. Real Example: Employee → Attendance

class Attendance(Base):
    __tablename__ = 'attendance'

    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    date = Column(Date, nullable=False)
    is_present = Column(Boolean, default=True)

    employee = relationship("Employee", back_populates="attendance_records")
python

class Employee(Base):
    # already defined
    attendance_records = relationship("Attendance", back_populates="employee")

