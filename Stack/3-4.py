class Stack:
    def __init__(self, ls=None):
        if ls is None:
            self.stack = []
        else:
            self.stack = ls

    # Push
    def push(self, i):
        self.stack.append(i)

    # Pop
    def pop(self):
        return self.stack.pop()

    # Peek
    def peek(self):
        return None if self.isEmpty() else self.stack[-1]

    # isEmpty
    def isEmpty(self):
        return True if self.stack == [] else False

    # Size
    def size(self):
        return len(self.stack)


def forest(lst):
    tree = Stack()
    for i in lst:
        command = i.split()
        if command[0] == "A":
            while not tree.isEmpty() and tree.peek() <= int(command[1]):
                tree.pop()
            tree.push(int(command[1]))
        elif command[0] == "B":
            print(tree.size())


inp = [e for e in input("Enter Input : ").split(",")]
forest(inp)
