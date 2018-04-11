#Challenge 3
class Shape():
    def what_am_i(self):
        print("I am a shape")

#Challenge 1
class Rectangle(Shape):
    def __init__(self, w,l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        return (self.width * 2) + (self.len * 2)
class Square(Shape):
    def __init__(self, s):
        self.side = s
    def calculate_perimeter(self):
        return (self.side * 4)
    #Challenge 2
    def change_size(self, w):
        self.side += w

rect = Rectangle(2, 4)
sqr = Square(4)
print(rect.calculate_perimeter())
print(sqr.calculate_perimeter())


#Challenge 2
sqr.change_size(-2)
print(sqr.calculate_perimeter())

#Challenge 3
rect.what_am_i()
sqr.what_am_i()

#Challenge 4
class Horse():
    def __init__(self, breed, racer, rider):
        self. breed = breed
        self. racer = racer
        self.rider = rider
class Rider():
    def __init__(self, name):
        self.name = name
ryan = Rider("Ryan")
horse = Horse('Arabian', True, ryan)

print("\nBreed: {}\nRacer: {}\nRider: {}\n".format(horse.breed, horse.racer, horse.rider.name))