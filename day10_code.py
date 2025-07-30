# main_app.py
import streamlit as st
from crud_employee import add_employee, get_all_employees
from crud_attendance import mark_attendance
from crud_payslip import generate_payslip

st.title("🧾 Employee Payroll Management System")

menu = st.sidebar.selectbox("Menu", ["Add Employee", "View Employees", "Mark Attendance", "Generate Payslip"])

if menu == "Add Employee":
    st.subheader("Add New Employee")
    name = st.text_input("Name")
    email = st.text_input("Email")
    department = st.text_input("Department")
    designation = st.text_input("Designation")
    salary = st.number_input("Salary")
    
    if st.button("Add"):
        add_employee(name, email, department, designation, salary)
        st.success("Employee added successfully.")

elif menu == "View Employees":
    st.subheader("Employee List")
    employees = get_all_employees()
    for emp in employees:
        st.write(f"{emp.id}: {emp.name} | {emp.email} | {emp.department}")

elif menu == "Mark Attendance":
    st.subheader("Mark Attendance")
    emp_id = st.number_input("Employee ID", step=1)
    status = st.selectbox("Status", ["Present", "Absent"])
    if st.button("Submit Attendance"):
        mark_attendance(emp_id, status)
        st.success("Attendance marked.")

elif menu == "Generate Payslip":
    st.subheader("Generate Payslip")
    emp_id = st.number_input("Employee ID", step=1)
    if st.button("Generate"):
        payslip = generate_payslip(emp_id)
        if payslip:
            st.write(payslip)
        else:
            st.warning("Payslip not available.")
#Note: This is just the base UI. You’ll connect all your CRUD logic from previous files.
