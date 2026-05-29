class Student:
    def __init__(self, name, grade, subject):
        self.name = name
        self.grade = grade
        self.subject = subject


# return a string like: "Tejas is in grade 7 studying Math"
    def report(self):
        return self.name + " is in grade " + str(self.grade) + " studying " + self.subject


# Create two students and print their reports
s1 = Student("Aarav", 6, "Coding")
s2 = Student("Priya", 7, "Math")
print(s1.report())
print(s2.report())