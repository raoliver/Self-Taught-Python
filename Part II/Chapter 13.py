#4 Pillars of ObjectOriented Programming

#Inheritance
class Shape():
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("""{} by {}
              """.format(self.width, self.len))

#Pass shape class to square as parameter inherits all functions and attributes // Child class of Shape
class Square(Shape):
    def area(self):
        return self.width * self.len
    def print_size(self):
        print("""I am {} by {}
              """.format(self.width, self.len))

# a_square = Square(20, 20)
# a_square.print_size()
# print(a_square.area())


class Dog ():
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
class Person():
    def __init__(self, name):
        self.name = name

ryan = Person("Ryan")
bent = Dog('Bentley', 'Lab', ryan)
print(bent.owner.name)