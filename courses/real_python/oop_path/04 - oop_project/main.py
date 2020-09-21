import hr
import employees
import productivity

manager = employees.Manager(1, 'Jose Contreras', 1500)
secretary = employees.Secretary(1, 'Laura Vergara', 750)
sales_guy = employees.SalesPerson(3, 'Pablo Espinoza', 1000, 250)
factory_worker = employees.FactoryWorker(3, 'Gustavo Cumare', 40, 20)


# we comment this because Employee is an Abstract Class, so It can be instaciated
# generic_employee = hr.Employee(4, 'Generic Employee')

# employees = [salary_employee, hourly_employee, commission_employee, generic_employee]
employees_list = [ manager, secretary, sales_guy, factory_worker ]


productivity_system = productivity.ProductivitySystem()
productivity_system.track(employees_list, 40)

payroll_system = hr.PayrollSystem()
payroll_system.calculate_payroll(employees_list)