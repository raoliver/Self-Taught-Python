# #Basic function definition
# def f (x):
#     return x + 1
# z = f(4)
#
# if z == 5:
#     print ( 'z is 5 ')
# else:
#     print('z is not 5')

##Age comparison with user
# age = input('Enter your age: ')
# int_age = int(age)
# if int_age < 21:
#     print('You are young!')
# else:
#     print('Wow, you are old!')

##even odd comparison
# def even_or_odd():
#     num = input('\nEnter a number: ')
#     num = int(num)
#     if (num % 2 == 0):
#         print('even')
#     else:
#         print('odd')
# even_or_odd()

#Challenge 1
def squared():
    """takes input from user, squares it and prints the result"""
    x = input('Enter a number: ')
    x = int(x)
    print(x**2)
squared()

#Challenge 2
def print_string(y):
    """converts input to a string and prints the result"""
    y = str(y)
    print(y)

y = input('Enter a string: ')
print_string(y)

#Challenge 3
def add_nums(x, y, z, a=0, b=1, c=2):
    """adds all numbers together
    a, b, c are optional values"""
    return x + y + z + a + b + c
num1 = 1
num2 = 4
num3 = 2
sum = add_nums(num1, num2, num3)
print(sum)

#Challenge 4
def div_func(x):
    """divides input by 2"""
    x = int(x)
    return x/2

def mult_func(y):
    """multiplies input by 4"""
    y = int(y)
    return y*4

a = 4
b = div_func(a)
result1 = mult_func(b)
print(result1)

#Challenge 5
def conversion_func(x):
    """converts a string to a float and returns result"""
    try:
        x = float(x)
    except ValueError:
        print('Invalid value')
    return x

num = input('Enter a float: ')
result3 = conversion_func(num)
