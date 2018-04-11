##Hangman Game set up
def hangman(word) :
    wrong = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')
    while wrong < len(stages) -1 :
        print('\n')
        msg = 'Guess a letter'
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong +=1
        print((' '.join(board)))
        e = wrong + 1
        print('\n'.join(stages[0: e]))
        if '__' not in board:
            print('You win!')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong]))
        print('You lose! It was {}.'.format(word))

##Word list and calling a random word and starting game
word_list = ['cat', 'dog', 'ball', 'toy']
import random
num = random.randint(0, 4)


hangman(word_list[num])
