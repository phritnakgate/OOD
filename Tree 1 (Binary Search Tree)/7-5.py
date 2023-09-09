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

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data < root.data:
                root.left = self._insert(root.left, data)
            else:
                root.right = self._insert(root.right, data)
        return root

    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self, val):
        is_in = True
        if val == self.root.data:
            print("Root")
            return
        q = Queue()
        q.enQueue(self.root)
        while not q.isEmpty():
            n = q.deQueue()
            if n.data == val:
                print("Inner")
            if n.left is not None:
                if n.left.data == val:
                    if n.left.left is None and n.left.right is None:
                        print("Leaf")
                        return
                    else:
                        print("Inner")
                        return
                q.enQueue(n.left)
            if n.right is not None:
                if n.right.data == val:
                    if n.right.left is None and n.right.right is None:
                        print("Leaf")
                        return
                    else:
                        print("Inner")
                        return
                q.enQueue(n.right)
        is_in = False
        if not is_in:
            print("Not exist")

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])

T.printTree(root)
T.checkpos(inp[0])