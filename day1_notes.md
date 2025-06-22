# Day 1 - SQLAlchemy Introduction

## Objective:
  * What is SQLAlchemy?
  * What is role of ORM (Object Relational Mapping)?
  * Learn how to connect to a database (SQLite).
  * Set up base and session for the project.

1. What is SQLAlchemy?
   SQLAlchemy is a powerful Python library used to interact with databases. It supports both:
   * SQLAlchemy Core-- Low-level SQL expressions.
   * SQLAlchemy ORM-- High-level, Python way of managing database tables using classes and objects.

2. What is ORM
   Object Relational Mapping is a technique where:
   * Database table - Python classes
   * Table row - Python objects

3. Database Choice: SQLite
   In development or Streamlit projects, SQLite is a good choice because:
   * It doesn't need a separate server
   * It's fast and lightweight
   * It stores data in a file

4. SQLAlchemy Setup Code
   * Install SQLAlchemy
     pip install sqlalchemy
   * Python Setup Code
     #see in day 1 code
     Code Explanation
       create_engine() # connect to the SQLite file or creates it if missing
       declarative_base() # used to define ORM models (your tables)
       sessionmaker() # creates sessions to interact with the database
       echo=True # shows SQL logs for debugging

## Day 1 Summary:
  * SQLAlchemy = Python toolkit for database handling
  * ORM = Maps Python classes to database tables
  * SQLite = Lightweight file-based database
  * Base, Engine, Session = core components to start usin ORM
