# Day 1 - SQLAlchemy Introduction

#Step 1: Install SQLAlchemy using pip
# pip install sqlalchemy 

# Step 2: Import creat_engine from SQLAlchemy 
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Create an SQLite database
DATABASE_URL = "salite:///employee_payroll.db"
engine = create_engine(DATABASE_URL, echo= True)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

print("Database and setup done successfully")
