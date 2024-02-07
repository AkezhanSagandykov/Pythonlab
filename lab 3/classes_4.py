class Point:
    def __init__(self, x1 = float(input()), y1 = float(input())):
        self.x1 = x1
        self.y1 = y1
    def display(self):
        return self.x1, self.y1
    def move(self, x_new = float(input()), y_new = float(input())):
        self.x_new = x_new
        self.y_new = y_new
        self.x1 += self.x_new
        self.y1 += self.y_new
        return self.x1, self.y1
    def distance(self, x2 = float(input()), y2 = float(input())):
        self.x2 = x2
        self.y2 = y2
        distance = ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**0.5
        return distance
a = Point()
print(a.display())
print(a.move())
print(a.distance())