# #FizzBuzz
# def fizz_buzz():
#     for i in range(1, 101):
#         if i & 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)
# fizz_buzz()
# print()

##Sequential Search
print('Sequential Search')
def ss(number_list, n):
    found = False
    for i in number_list:
        if i == n:
            found = True
            break
    return found
numbers = range(0, 100)
s1 = ss(numbers, 2)
print(s1)
s2 = ss(numbers, 202)
print(s2)
print()

##Palindrome
print('Palindrome')
def palindrome(word):
    word = word.lower()
    return word[::-1] == word #Reverses word
print(palindrome('Mother'))
print(palindrome('Mom'))
print()

##Anagram
print('Anagram')
def anagram(w1, w2):
    w1 = w1.lower()
    w2 = w2.lower()
    return sorted(w1) == sorted(w2)

print(anagram('iceman', 'cinema'))
print(anagram('leaf', 'tree'))
print()

##Count Character Occurrences
print('Character Count Occurrences')
def count_characters(string):
    count_dict = {}
    for c in string:
        if c in count_dict:
            count_dict[c] +=1
        else:
            count_dict[c] = 1
    print(count_dict)

count_characters('Dynasty')
print()
##Recursion
print('Recursion')
#Breaking the problem up into smaller pieces until it can be easily solved
def bottles_of_beer(bob):
    """Prints 99 bottles of beer on the wall lyrics. :param bob: Must be a positive integer"""
    #Law 1: Base Case of recursion
    if bob < 1:
        print("""No more bottles of beer on the wall.
        No more bottles of beer.""")
        return
    tmp = bob
    #Law 2: Decrements value to move towards base case
    bob -= 1
    print("""{} bottles of beer on the wall. {}
                bottles of beer. Take one down, pass
                it around, {} bottles of beer on the wall.""".format(tmp,tmp,bob))
    #Law 3: Function calls it self recursively
    bottles_of_beer(bob)

bottles_of_beer(99)