#Working with Files

#writing to file 'python.txt'
with open("python.txt", 'w') as f:
    f.write('Hi from Python!')

#reading from file 'python.txt' and saving to variable file
file = []
with open('python.txt', 'r') as f:
    file.append(f.read())
print(file)


#Challenge 1
with open('/Users/raoliver/rpro.log', 'r') as f:
    print(f.read())

#Challenge 2
answer = input('What is your name? ')
with open('answer.txt', 'w') as f:
    f.write(answer)

#Challenge 3
movies = [['Top Gun', 'Risky Business', 'Minority Report'],
        ['Titanic', 'The Revenant', 'Inception'],
        ['Training Day', 'Man on Fire', 'Flight']]
import csv
with open('movie.csv', 'w') as f:
    w = csv.writer(f, delimiter=',')
    for i in movies:
        w.writerow(i)