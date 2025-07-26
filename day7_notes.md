# Day 7: Payslip Table (Notes)

## 🎯 Goal
Create and manage a payslip table that:
- Calculates salary using attendance
- Stores salary per month
- Is linked to each employee

## 🔁 Concepts
- One-to-Many relationship (Employee → Payslip)
- `func.count`, `extract` for attendance counting
- Auto-calculation using per-day salary
- Preventing duplicate payslips

## 🧱 Payslip Table Schema

| Column        | Type     | Description                   |
|---------------|----------|-------------------------------|
| id            | Integer  | Primary key                   |
| employee_id   | FK       | Linked to employee            |
| month         | Integer  | Month for salary              |
| year          | Integer  | Year for salary               |
| base_salary   | Float    | Per-day base salary           |
| present_days  | Integer  | Total presents in the month   |
| absent_days   | Integer  | Total absents in the month    |
| total_salary  | Float    | present_days × base_salary    |

## 🔧 Steps
1. Add `Payslip` model in `models.py`
2. Link it to `Employee` using `relationship`
3. Use `Attendance` table to get monthly presents/absents
4. Calculate total salary
5. Prevent duplicate entries for same month/year

## ✅ Output Example
Monika - 7/2025 - ₹23000
Ravi - 7/2025 - ₹20000
