##Stack
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

#Challenge 1
rev_stack = Stack()
reverse = ''
for c in 'yesterday':
    rev_stack.push(c)
for i in range(len(rev_stack.items)):
    reverse += rev_stack.pop()
print(reverse)


#Challenge 2
list = [1, 2, 3, 4, 5]
rev_list = []

new_stack = Stack()
for i in list:
    new_stack.push(i)
for x in range(len(new_stack.items)):
    rev_list.append(new_stack.pop())
print(rev_list)