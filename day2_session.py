 # day2_create_employee_table.py
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, sessionmaker
import datetime 

# step 1: Database cnnection
DATABASE_URL = "sqlite:///employee_payroll.db"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# step 2: Define the Employee model
class Employee(Base):
    __tablename__= 'employee'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    department = Column(String(50))
    designation = Column(String(50))
    salary = Column(Float)
    joining_date = Column(Date, default=datetime.date.today)

    def __repr__(self):
        return f"<Employee(name= '{self.name}',email='{self.email}')>"

 # step 3: Create the table   
Base.metadata.create_all(bind=engine)

# Step 4: Insert sample data
session = SessionLocal()
new_employee = Employee(
    name="Ravi Kumar",
    email="ravi@example.com",
    department="HR",
    designation="Manager", 
    salary=50000.0,
    joining_date=datetime.date(2022, 5, 2)
)
session.add(new_employee)
session.commit()
session.close()

print("Employee table created and one record inserted.")

