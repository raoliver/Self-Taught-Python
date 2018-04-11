#Challenge 1
shows=['The Walking Dead', 'Entourage', 'The Sopranos', 'The Vampire Diaries']
for show in shows:
    print(show)

#Challenge 2
for i in range(25, 51):
    print(i)

#Challenge 3
index = 0
for show in shows:
    print(index, show)
    index +=1

#Challenge 4
num_list =[1, 2, 3]
while True:
    a = input('Enter a number or press q to quit: ')
    if a == 'q':
        break
    try:
        a = int(a)
    except ValueError:
        print('Please try a number or type q to quit')
    if a in num_list:
        print('You guessed correctly!')
    else:
        print('Wrong')

#Challenge 5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
product = []

for i in list1:
    for j in list2:
        product.append(i * j)
print(product)