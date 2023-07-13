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
        return self.stack[-1]

    # isEmpty
    def isEmpty(self):
        if not self.stack:
            return False
        else:
            return True

    # Size
    def size(self):
        return len(self.stack)


def postFixeval(exp):
    s = Stack()
    op = ["+", "-", "*", "/"]
    for i in exp:
        if i not in op:
            s.push(int(i))
        else:
            result = 0
            if i == op[0]:
                result += s.peek()
                s.pop()
                result += s.peek()
                s.pop()
                s.push(result)
            elif i == op[1]:
                result = s.peek()
                s.pop()
                result -= s.peek()
                s.pop()
                s.push(-result)
            elif i == op[2]:
                result = 1
                result *= s.peek()
                s.pop()
                result *= s.peek()
                s.pop()
                s.push(result)
            elif i == op[3]:
                result = s.peek()
                s.pop()
                eiei = s.peek() / result
                s.pop()
                s.push(eiei)
    return s.peek()


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

print("Answer : ", '{:.2f}'.format(postFixeval(token)))
