class Shape:
    def area_default(self):
        return 0
class Rectangle(Shape):
    def __init__(self):
        self.length = float(input())
        self.width = float(input())
    def area(self):
        return self.length * self.width
a = Rectangle()
print(a.area_default())
print(a.area())