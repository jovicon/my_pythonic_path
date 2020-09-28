from productivity import ProductivitySystem
from hr import PayrollSystem
from contacts import AddressBook

# from hr import (
#     SalaryPolicy,
#     CommissionPolicy,
#     HourlyPolicy
# )
# from productivity import (
#     ManagerRole,
#     SecretaryRole,
#     SalesRole,
#     FactoryRole
# )

class EmployeeDataBase:
    def __init__(self):
        self._employees = [
            {
                'id':1,
                'name': 'Mary Poppins',
                'role': 'manager'
            }
        ]

        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)

class Employee:
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = None
        self.role = role
        self.payroll = payroll

    def work(self, hours):
        duties = self.role.work(hours)
        print(f'Employee {self.id} - {self.name}:')
        print(f'- {duties}')
        print('')
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()

# class Manager(Employee, ManagerRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_Salary):
#         SalaryPolicy.__init__(self, weekly_Salary)
#         super().__init__(id, name)



# class Secretary(Employee, SecretaryRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_Salary):
#         SalaryPolicy.__init__(self, weekly_Salary)
#         super().__init__(id, name)



# class SalesPerson(Employee, SalesRole, CommissionPolicy):
#     def __init__(self, id, name, weekly_Salary, commission):
#         CommissionPolicy.__init__(self, weekly_Salary, commission)
#         super().__init__(id, name)



# class FactoryWorker(Employee, FactoryRole, CommissionPolicy):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         CommissionPolicy.__init__(self, hours_worked, hour_rate)
#         super().__init__(id, name)


# class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
#     def __init__(self, id, name,hours_worked, hour_rate):
#         HourlyPolicy.__init__(self, hours_worked, hour_rate)
#         super().__init__(id, name)