from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    employees = relationship("Employee", back_populates="department")

class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship("Department", back_populates="employees")
    attendance_records = relationship("Attendance", back_populates="employee")

class Attendance(Base):
    __tablename__ = 'attendance'
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    date = Column(Date, nullable=False)
    is_present = Column(Boolean, default=True)

    employee = relationship("Employee", back_populates="attendance_records")

# Setup
engine = create_engine('sqlite:///epms.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
