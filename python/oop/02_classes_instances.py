class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amount)

print(Employee.num_of_emps)
emp_1 = Employee('Tejas', 'Dutt', 150000)
emp_2 = Employee('Test', 'User', 99)

print(Employee.num_of_emps)

# print(Employee.__dict__)

# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)


# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)