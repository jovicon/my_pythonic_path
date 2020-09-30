from hr import PayrollSystem
from productivity import ProductivitySystem
from employees import EmployeeDataBase

productivity_system = ProductivitySystem()
payroll_system = PayrollSystem()
employee_database = EmployeeDataBase()

employees = employee_database.employees()
productivity_system.track(employees, 40)
payroll_system.calculate_payroll(employees)
