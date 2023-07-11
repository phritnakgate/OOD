class Stack:
    def __init__(self):
        self.stack = []

    def push(self, i):
        self.stack.append(i)

    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.stack.pop()

    def isEmpty(self):
        if not self.stack:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)

    #


print(" *** Stack implement by Python list***")
ls = [e for e in input("Enter data to stack : ").split()]
s = Stack()
for e in ls:
    s.push(e)
print(s.size(), "Data in stack : ", s.stack)
while not s.isEmpty():
    s.pop()
print(s.size(), "Data in stack : ", s.stack)
