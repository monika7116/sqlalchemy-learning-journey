✅ Day 8 – Advanced Joins in SQLAlchemy ORM
🔹 What is a JOIN?
SQL join helps you combine data from multiple tables based on a related column.

In SQLAlchemy, you can use .join() and .outerjoin() for this purpose.

🔸 Why Use Joins in Your Project?
Taaki aap ek hi query me:

Employee ka naam

Uski attendance
Uska salary info
ek saath fetch kar sako.

🔸 Types of Joins in SQLAlchemy:
Type	Description	SQLAlchemy Function
INNER JOIN	Sirf un rows ko laata hai jinka match dono tables me ho	.join()
LEFT JOIN	Left table ke sabhi rows laata hai, chahe match ho ya na ho	.outerjoin()

🧱 Tables Required (from earlier Days):
Employee

Attendance

Payslip

🔍 INNER JOIN Example:

session.query(Employee.name, Attendance.date, Attendance.status).join(Attendance).all()
Sirf un employees ko laata hai jinke attendance record hai.

🔍 LEFT OUTER JOIN Example:

session.query(Employee.name, Attendance.date, Attendance.status).outerjoin(Attendance).all()
Sabhi employees ko laata hai, chahe unki attendance ho ya nahi.

🔍 JOIN with Payslip Table:

session.query(Employee.name, Payslip.month, Payslip.net_pay).join(Payslip).all()
Employee ke naam ke saath uska payslip details bhi dikhata hai.

📌 Important Points:
Use .join() jab aapko only matching records chahiye ho.

Use .outerjoin() jab sabhi records chahiye ho from left table.

Use .filter() for date/month conditions.

Don't forget to close session: session.close()

🧠 Bonus: Chhoti Tips
.join() internally uses ForeignKey relationships.

Use .all() to get all rows, .first() for one row.

