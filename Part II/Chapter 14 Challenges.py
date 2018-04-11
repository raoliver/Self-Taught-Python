#Challenge 1
class Square():
    square_list = []

    def __init__(self, s):
        self.side = s
        self.square_list.append(self.side)

    #Challenge 2
    def print_size(self):
        print("""{} by {} by {} by {}""".format(self.side, self.side, self.side, self.side))

s1 = Square(4)
s2 = Square(2)
s3 = Square(4)
print(s1.print_size())

#Challenge 3

def compare_objects(x, y):
    return x is y
print(compare_objects(s1, s2))#False
print(compare_objects("a", "a"))#True