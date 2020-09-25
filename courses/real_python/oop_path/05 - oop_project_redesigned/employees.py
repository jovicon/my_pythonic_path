from hr import (
    SalaryPolicy,
    CommissionPolicy,
    HourlyPolicy
)
from productivity import (
    ManagerRole,
    SecretaryRole,
    SalesRole,
    FactoryRole
)

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Manager(Employee, ManagerRole, SalaryPolicy):
    def __init__(self, id, name, weekly_Salary):
        SalaryPolicy.__init__(self, weekly_Salary)
        super().__init__(id, name)



class Secretary(Employee, SecretaryRole, SalaryPolicy):
    def __init__(self, id, name, weekly_Salary):
        SalaryPolicy.__init__(self, weekly_Salary)
        super().__init__(id, name)



class SalesPerson(Employee, SalesRole, CommissionPolicy):
    def __init__(self, id, name, weekly_Salary, commission):
        CommissionPolicy.__init__(self, weekly_Salary, commission)
        super().__init__(id, name)



class FactoryWorker(Employee, FactoryRole, CommissionPolicy):
    def __init__(self, id, name, hours_worked, hour_rate):
        CommissionPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)


class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
    def __init__(self, id, name,hours_worked, hour_rate):
        HourlyPolicy.__init__(self, hours_worked, hour_rate)
        super().__init__(id, name)