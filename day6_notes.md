Goal of the Day
To generate attendance summaries (e.g., number of presents/absents) for each employee using SQLAlchemy ORM.

This is useful for:

Calculating salaries based on attendance

Generating monthly reports

Showing dashboard summaries

🔁 Key Concepts
Concept	Description
func.count()	#SQLAlchemy function for counting records
group_by()	#Groups rows based on a column (like employee_id)
filter() and filter_by()	#For filtering specific month/date range
datetime / extract()	#Extract month/year from date column

🔧 Step-by-Step Guide
✅ 1. Import Tools
python
Copy code
from sqlalchemy import func, extract
from datetime import date
✅ 2. Count Present Days for Each Employee
python

summary = session.query(
    Employee.name,
    func.count(Attendance.id).label('present_days')
).join(Attendance).filter(Attendance.is_present == True).group_by(Employee.id).all()

for name, present_days in summary:
    print(f"{name} was present {present_days} days.")
✅ 3. Monthly Attendance Summary
python

month = 7   # July
year = 2025

summary = session.query(
    Employee.name,
    func.count(Attendance.id).label('present_days')
).join(Attendance).filter(
    Attendance.is_present == True,
    extract('month', Attendance.date) == month,
    extract('year', Attendance.date) == year
).group_by(Employee.id).all()

for name, present_days in summary:
    print(f"{name} was present in {month}/{year}: {present_days} days")
✅ 4. Get Present and Absent Counts for Each Employee
python

employees = session.query(Employee).all()
month = 7
year = 2025

for emp in employees:
    present = session.query(func.count(Attendance.id)).filter(
        Attendance.employee_id == emp.id,
        Attendance.is_present == True,
        extract('month', Attendance.date) == month,
        extract('year', Attendance.date) == year
    ).scalar()

    absent = session.query(func.count(Attendance.id)).filter(
        Attendance.employee_id == emp.id,
        Attendance.is_present == False,
        extract('month', Attendance.date) == month,
        extract('year', Attendance.date) == year
    ).scalar()

    print(f"{emp.name}: Present = {present}, Absent = {absent}")
