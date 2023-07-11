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


def managestack(command, stack):
    choice = command.split()[0]
    value = None
    if choice != "P":
        value = int(command.split()[1])
    temp = Stack()

    if choice == "A":
        stack.push(value)
        print(f"Add = {value}")
    elif choice == "P":
        if stack.stack:
            temp.stack = stack.stack
            print(f"Pop = {temp.stack[-1]}")
            stack.pop()
        else:
            print(-1)
    elif choice == "D":
        if stack.stack:
            for i in range(stack.size()-1, -1, -1):
                item = stack.stack[i]
                if item != value:
                    temp.push(item)
                    stack.pop()
                else:
                    stack.pop()
                    print(f"Delete = {value}")
            for j in range(temp.size()-1, -1, -1):
                stack.push(temp.stack[j])
        else:
            print(-1)
    elif choice == "LD":
        if stack.stack:
            for i in range(stack.size() - 1, -1, -1):
                item = stack.stack[i]
                if item >= value:
                    temp.push(item)
                    stack.pop()
                else:
                    stack.pop()
                    print(f"Delete = {item} Because {item} is less than {value}")
            for j in range(temp.size() - 1, -1, -1):
                stack.push(temp.stack[j])
        else:
            print(-1)
    elif choice == "MD":
        if stack.stack:
            for i in range(stack.size() - 1, -1, -1):
                item = stack.stack[i]
                if item <= value:
                    temp.push(item)
                    stack.pop()
                else:
                    stack.pop()
                    print(f"Delete = {item} Because {item} is more than {value}")
            for j in range(temp.size() - 1, -1, -1):
                stack.push(temp.stack[j])
        else:
            print(-1)


ls = [e for e in input("Enter Input : ").split(",")]
st = Stack()
for i in ls:
    managestack(i, st)
print("Value in Stack =", st.stack)
