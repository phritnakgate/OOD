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

    def delete(self, r, data):
        self.root = BinarySearchTree._deleteNodeS(self.root, data)

    # def _deleteNodeP(root: Node, key: int):
    #     if root is None: return root
    #     if int(key) < int(root.data):
    #         root.left = BinarySearchTree._deleteNodeP(root.left, key)
    #     elif int(key) > int(root.data):
    #         root.right = BinarySearchTree._deleteNodeP(root.right, key)
    #     else:
    #         if root.left is None or root.right is None:
    #             root = root.left if root.right is None else root.right
    #         else:
    #             temp = root.left
    #             while temp.right is not None:
    #                 temp = temp.right
    #             root.data = temp.data
    #             root.left = BinarySearchTree._deleteNodeP(root.left, temp.data)
    #     return root

    def _deleteNodeS(root: Node, key: int):
        if root is None: return root
        if int(key) < int(root.data):
            root.left = BinarySearchTree._deleteNodeS(root.left, key)
        elif int(key) > int(root.data):
            root.right = BinarySearchTree._deleteNodeS(root.right, key)
        else:
            if root.left is None or root.right is None:
                root = root.left if root.right is None else root.right
            else:
                temp = root.right
                while temp.left is not None:
                    temp = temp.left
                root.data = temp.data
                root.right = BinarySearchTree._deleteNodeS(root.right, temp.data)
        return root


def printTree90(node, level=0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)


traversal = []


def inOrder(root):
    if root is not None:
        # Left Subtree
        inOrder(root.left)
        # Root
        traversal.append(root.data)
        # Right Subtree
        inOrder(root.right)


tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in data:
    traversal = []
    inOrder(tree.root)
    if i[0] == "i":
        print(f"insert {i[2:]}")
        tree.insert(int(i[2:]))
        printTree90(tree.root)
    elif i[0] == "d":
        print(f"delete {i[2:]}")
        if tree.root is None:
            print("Error! Not Found DATA")
        else:
            if int(i[2:]) not in traversal:
                print("Error! Not Found DATA")
                printTree90(tree.root)
            else:
                tree.delete(tree.root, int(i[2:]))
                printTree90(tree.root)
