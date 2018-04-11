##More OOP

class Rectangle():
    recs = []#class variable

    def __init__(self, w, l):
        self.width = w#Instance variable
        self.len = l
        self.recs.append((self.width, self.len))#Appends the object to the list recs

    def print_size(self):
        print("""{} by {}""".format(self.width, self.len))

r1 = Rectangle(10, 24)
r2 = Rectangle(20, 40)
r3 = Rectangle(100, 200)

print(Rectangle.recs)

##Magic Methods
class Lion:
    def __init__(self, name):
        self.name = name

    #Overrides inherited __repr__ method and prints name
    def __repr__(self):
        return self.name

lion = Lion('Dilbert')
print(lion)

#Another Magic Method Example
class AlwaysPositive:
    def __init__(self, number) :
        self.n = number

    ##overrides the add function to return the absolute value of 2 numbers added together
    def __add__(self, other):
        return abs(self.n +
                   other.n)

x = AlwaysPositive(-20)
y = AlwaysPositive(10)

print(x + y)


