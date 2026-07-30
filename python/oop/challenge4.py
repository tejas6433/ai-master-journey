class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0     # base default, overridden by children

    def __str__(self):
        return f"{self.name}: area = {self.area()}"
    #  → add a __eq__ method to Shape that compares area() 
    def __eq__(self, shp):
        if self.area() > shp.area():
            return f"{self.name}: area = {self.area()} is greater than {shp.name}: area = {shp.area()}"
        elif self.area() < shp.area():
            return f"{self.name}: area = {self.area()} is less than {shp.name}: area = {shp.area()}"
        else:
            return f"{self.name}: area = {self.area()} is exaclty same as {shp.name}: area = {shp.area()}"


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Rectangle")
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return round(3.14159 * self.radius ** 2, 2)


# YOUR TASK:
#  → create a Rectangle(4, 5) and a Circle(3)
rect_1 = Rectangle(4,5)
cir_1 = Circle(3)


#  → print both directly (uses __str__)
print(rect_1)
print(cir_1)
#  → print isinstance(rect, Shape) -> should be True
print(isinstance(rect_1,Shape))
#  → add a __eq__ method to Shape that compares area() 

#    between two shapes, test it
print(cir_1.__eq__(rect_1))
print(rect_1.__eq__(cir_1))
