##For Loops
name = "Ryan"
for x in name:
    print(x)

#printing keys
people = {'G. Bluth II': 'A. Development',
          'Barney':'HIMYM','Dennis':'Always Sunny'}
for character in people:
    print(character)

tv = ['GOT', 'Narcos', 'Vice']
coms = ['Arrested Development', 'friends', 'Always Sunny']

#changing items using loops
i = 0
for show in tv: #Caps all letters in the list
    new = tv[i]
    new =new.upper()
    tv[i] = new
    i += 1
print(tv)

#same as above using enumerate
for i, show in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new
print(tv)

##While Loops
x = 10
while x > 0:
    print ('{}'.format(x))
    x -= 1
print('Happy New Year!')

qs = ['What is your name?', 'What is your favorite color?', 'What is your quest?']
n = 0
while True:
    print ('Type q to quit')
    a = input(qs[n])
    if a =='q':
        break
    n = (n + 1) % 3

#Nested loops
list1= [1, 2, 3, 4]
list2= [5, 6, 7, 8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)

