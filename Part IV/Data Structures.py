##########################
#Stacks
##LIFO (Last In First Out)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) -1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
print(stack.is_empty())

# stack.push(2)
# print(stack.peek())
# item = stack.pop()
# print(item)
# print(stack.is_empty())

# for i in range(0, 10)
#     stack.push(i)
# print(stack.peek())
# print(stack.size())

##Reversing a string using a stack
for c in 'Hello':
    stack.push(c)
reverse = ""
for i in range(len(stack.items)):
    reverse += stack.pop()
print(reverse+'\n')


############################################################################
##Queues
#FIFO (First In First Out)
import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    #Ticket Simulator
    def simulate_line(self, till_show, max_time):
        pq = Queue()
        tix_sold = []

        for i in range(10):
            pq.enqueue('person' + str(i))
        t_end = time.time() + till_show
        now = time.time()
        while now < t_end and not pq.is_empty():
            now = time.time()
            r = random.randint(0, max_time)
            time.sleep(r)
            person = pq.dequeue()
            print(person)
            tix_sold.append(person)
        return tix_sold

# a_queue = Queue()

# for i in range(5):
#     a_queue.enqueue(i)
# print(a_queue.size())
#
# for i in range(5):
#     print(a_queue.dequeue())
# print()
#
# print(a_queue.size())

##Ticket Simulator
queue = Queue()
sold = queue.simulate_line(5, 1)
print(sold)