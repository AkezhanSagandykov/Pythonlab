class Shape:
    def area_default(self):
        return 0
class Square(Shape):
    def __init__(self, length = float(input())):
        self.length = length
    def area(self):
        area = self.length**2
        return area
a = Square()
print(a.area_default())
print(a.area())
