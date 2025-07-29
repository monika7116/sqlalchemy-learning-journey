1. What are Reusable Queries?
Reusable queries are functions that allow you to write SQLAlchemy code once and use it again and again whenever needed.

Instead of repeating the same query code every time, you make a function like:


def get_employee_by_email(email):
    ...
So next time you need to search an employee by email — just call this function!

 2. Why Use Reusable Queries? (Benefits)
 Feature	 Benefit
Repeatable Code	No need to write same query again & again
Clean Code	Code looks neat and organized
Easy Debugging	If there’s an error, fix it in one place
Reusable in UI	Connects easily with Streamlit/Flask etc.
Better Maintenance	Easy to update later

 3. Where to write these queries?

crud_employee.py
Put all your reusable functions inside this file — later, import and use them in your main app or script.

 4. Steps to Write Reusable Query Functions
 Step 1: Use SessionLocal() inside a with block
Step 2: Write the query using SQLAlchemy
 Step 3: Return or print the result
 Step 4: Handle if data is not found (optional)

 5. Most Useful Reusable Functions (for your project)
 Function Name	 Purpose
add_employee()	Add a new employee
get_all_employees()	Show all employees
get_employee_by_email()	Search employee using email
update_salary()	Update salary for specific employee
delete_employee_by_id()	Delete employee by ID

 6. Best Practices
Always use with SessionLocal() as session: — this closes the session safely

Add proper error checking: what if employee not found?

Keep the function logic short and clear

Test your functions separately

 Example Function: Get Employee by Email

def get_employee_by_email(email):
    with SessionLocal() as session:
        return session.query(Employee).filter_by(email=email).first()
 How to use the function

from crud_employee import get_employee_by_email

emp = get_employee_by_email("ravi@example.com")
if emp:
    print("Found:", emp.name)
else:
    print("No employee found.")
📌 Final Tip:
These functions will be super useful in Day 10 when you integrate everything into Streamlit.

