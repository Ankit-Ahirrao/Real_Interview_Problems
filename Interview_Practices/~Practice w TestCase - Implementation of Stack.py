# -----------------------------------------------------------

# Implement Stack class with find(item) 
# that returns index of the item in the stack.
# implement push(item) and pop()
# return -1 if an item isnt found

# Make stack
    # push
    # pop
    # search item

class Stack:
    def __init__(self):
        self.stack = []
        self.location = defaultdict(list)
        self.leng = 0

    def push (self, item):
        self.stack.append(stack)
        self.location[item].append(self.leng) 
        self.leng += 1

    def pop (self):
        if leng <= 0: 
            return -1
        item = self.stack.pop()
        self.location[item].pop()
        self.leng -= 1
        return item

    def find(self, item):
        if self.location[item]:
            return self.location[item][-1]
        return -1