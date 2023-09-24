class Tree:
    class Node:
        def __init__(self, data=None):
            if data is None:
                self.data = None
            else:
                self.data = data
            self.left = self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, root, data):
        if root is None:
            return self.Node(data)
        else:
            if data < root.data:
                root.left = self._insert(root.left, data)
            else:
                root.right = self._insert(root.right, data)
        return root


inp = input("Enter Input : ").split("/")
num_van = int(inp[0])
day = [int(i) for i in inp[1].split(" ")]

all_van = {}
for i in range(int(num_van)):
    all_van.update({i + 1: 0})
customer = 1

while len(day) > 0:
    T = Tree()
    all_van = dict(sorted(all_van.items(), key=lambda x: x[::-1]))
    for i in all_van.items():
        T.insert(list(i))
    T.root.data[1] += day[0]
    all_van[T.root.data[0]] += day[0]
    print(f"Customer {customer} Booking Van {T.root.data[0]} | {day[0]} day(s)")
    day.pop(0)
    customer += 1
