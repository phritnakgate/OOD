class Queue:
    def __init__(self):
        self.queue = []

    def enQueue(self, data):
        self.queue.append(data)

    def deQueue(self):
        return self.queue.pop(0)

    def isEmpty(self):
        return self.queue == []

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


def father(r, data):
    q = Queue()
    q.enQueue(r)
    while not q.isEmpty():
        n = q.deQueue()
        if n.data == data:
            return "None Because " + str(data) + " is Root"
        else:
            if n.left is not None:
                if n.left.data == data:
                    return n.data
                q.enQueue(n.left)
            if n.right is not None:
                if n.right.data == data:
                    return n.data
                q.enQueue(n.right)
    return "Not Found Data"



tree = BinarySearchTree()
data = input("Enter Input : ").split("/")
for e in data[0].split():
    tree.create(e)
printTree90(tree.root)
print(father(tree.root, data[1]))
