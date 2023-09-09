class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return self.stack == []

    def size(self):
        return len(self.stack)


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


def findBelow(tree, val):
    # Depth-First Order : InOrder
    inOrder(tree.root)
    below = ""
    for i in range(len(traversal)):
        if traversal[i] < val:
            below += str(traversal[i])
            below += " "
    return below


traversal = []


def inOrder(root):
    if root is not None:
        # Left Subtree
        inOrder(root.left)
        # Root
        traversal.append(root.data)
        # Right Subtree
        inOrder(root.right)


T = BST()
inp = input('Enter Input : ').split("|")
tr_element = [int(i) for i in inp[0].split(" ")]
for i in tr_element:
    root = T.insert(i)

T.printTree(root)
print("-" * 50)
bel = findBelow(T, int(inp[1]))
if not bel:
    print(f"Below {inp[1]} : Not have")
else:
    print(f"Below {inp[1]} : {bel}")
