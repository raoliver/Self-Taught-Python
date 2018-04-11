import math

#Challenge 1
class Apple():
    def __init__(self, c, w, t, s):
        """weight is in oz."""
        self.color = c
        self.weight = w
        self.type = t
        self.size = s
apple = Apple('Green', 4, 'Granny Smith', 'Small')
print('Color: {}\n Weight(oz.): {}\n Type: {}\n Size: {}\n'.format(apple.color, apple.weight, apple.type, apple.size))

#Challenge 2
class Circle():
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * (self.radius ** 2)
circle = Circle(2)
print(circle.area())

#Challenge 3
class Triangle():
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def area(self):
        return (self.base*self.height) / 2
tri = Triangle(2, 4)
print(tri.area())

#Challenge 4
class Hexagon():
    def __init__(self, a, b, c, d, e, f):
        self.s1 = a
        self.s2 = b
        self.s3 = c
        self.s4 = d
        self.s5 = e
        self.s6 = f
    def calculate_perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6
hex = Hexagon(1, 2, 3, 4, 5, 6)
print(hex.calculate_perimeter())



