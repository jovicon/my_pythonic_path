import hr

salary_employee = hr.SalaryEmployee(1, 'Jose Contreras', 1500)
hourly_employee = hr.HourlyEmployee(2, 'Laura Vergara', 40, 15)
commission_employee = hr.CommissionEmployee(3, 'Pablo Espinoza', 1000, 250)

employees = [salary_employee, hourly_employee, commission_employee]

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees)