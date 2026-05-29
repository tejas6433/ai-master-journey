# Python Object-Oriented Programming


class Employee:
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Tejas', 'Dutt', 150000)
emp_2 = Employee('Test', 'User', 99)


print(Employee.fullname(emp_1))
print(emp_2.fullname())