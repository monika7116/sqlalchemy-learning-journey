# Learning Goals:
  1. Define you first ORMmodel (class-based table)
  2. Creat an actual database table using SQLAlchemy
  3. insert a record into the table
  4. Understand the structure of a model (columns, typess, constrains)

* The first and most important table is 'Employee' table . stores: name, email, department, designation, salary, and joining date.

* Engine+Session Setup
  1. creat_engine: Connects to SQLite file database.
  2. Declarative_base():Base class for all models.
  3. sessionmaker():Allows you to open a connection (session) with the database.

* Employee Model
    Each column in the table is written as a python class variable:
    column name       Type       Explanation
  1. id                integer    Auto-increment primary key
  2. name              string     Required field (nullable=False)
  3. email             string     Must be uniaue
  4. department        string     Optional department field
  5. designation       string     Job title (eg. Manager)
  6. salary            Float      Basic salary
  7. joining_date      Date       Default is today

* Table Creation
  Base.metadata.create_all(bind=engine)
  This command creates the employee table in your database if it doesn't already exist.

* Inserting a Record
  session = SessionLocal()
  session.add(new_employee)
  session.commit()
  session.close()

  Create a session then add the object then commit(save) then close the session


# Day 2 Summary 

topics:                              Description
Model Class                          Define 'Employee' model as a table
Columns                              Used ' column' objects to define structure
Table Creation                       Use ' Base.metadata.create_all()' 
insert                               Use 'session.add()' and 'session.commit()'
