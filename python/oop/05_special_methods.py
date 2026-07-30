class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self. last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname (self) :
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int (self.pay * self.raise_amt)


    def __repr__(self):
        return "Employee('{}', '{}','{}')".format(self.first, self.last, self.pay)
  
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)

print(len(emp_1))



# print(emp_1.__repr__())

# print(emp_1.__str__())




# print(mgr_1.email)
# mgr_1.add_emp(dev_2)

# mgr_1.print_emps()

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(1+2)
# print(int.__add__(1,2))