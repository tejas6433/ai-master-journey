import datetime


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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# print(Employee.num_of_emps)
emp_1 = Employee('Tejas', 'Dutt', 150000)
emp_2 = Employee('Test', 'User', 99)


my_date = datetime.date(2026, 10, 26)

print(Employee.is_workday(my_date))










# emp_str_1 = "jaskaran-singh-190000"
# emp_str_2 = "dev-beri-200000"
# emp_str_3 = "guri-sidhu-160000"

# new_emp_1 = Employee.from_string(emp_str_1)


# print(new_emp_1.email)
# print(new_emp_1.pay)






# print(Employee.num_of_emps)

# print(Employee.__dict__)

# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)


# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)