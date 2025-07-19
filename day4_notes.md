 Part 1: Understanding the Relationships
🔹 Many-to-One
Actually, this is the same as One-to-Many, just seen from the "many" side.

Example:

Many Employees → Belong to One Department

Already covered on Day 3!

🔸 One-to-One Relationship
This means:

One row in Table A ↔ Exactly one row in Table B

Example in Payroll System:

One Employee → One Permanent Address

One Employee → One Bank Account Details

🧱 Part 2: One-to-One Relationship in SQLAlchemy
SQLAlchemy doesn’t have a direct one-to-one class — instead, we create:

A unique foreign key

A relationship() with uselist=False

💡 Use Case in Project:
One Employee ↔ One SalaryAccount

✅ Final Notes Summary
markdown
Copy
Edit
# Day 4: One-to-One Relationship – SQLAlchemy ORM

## What is One-to-One?
A relationship where one record in Table A is related to exactly one record in Table B.

## How to Implement:
- Use `ForeignKey(unique=True)` in B table
- Set `uselist=False` in `relationship()
