class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None:  # Locating tail + finding size
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self):
        st = str(self.head)
        t = self.head
        while t.next is not None:
            t = t.next
            st += "->"
            st += str(t)
        return st

    def append(self, data):
        n = Node(data)
        if self.head is None:
            self.head = self.tail = n
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = n
            self.tail = n
        self.size += 1


inp = input("Enter input : ").split(",")
LL = LinkedList()
found_loop = False
for i in inp:
    if "A" in i:
        data = i.split(" ")[1]
        LL.append(data)
        print(LL)
    elif "S" in i:
        id1, id2 = i.split(" ")[1].split(":")[0], i.split(" ")[1].split(":")[1]
        id1 = int(id1)
        id2 = int(id2)
        # Check Empty
        if LL.size == 0:
            print("Error! {list is empty}")
        else:
            # Check if input more than index
            if LL.size - 1 < id1:
                print("Error! {index not in length}: " + str(id1))
                continue
            # Check if pointed position more than index -> append
            if id2 > LL.size - 1:
                LL.append(id2)
                print(f"index not in length, append : {id2}")
            # Check if point to itself
            elif id1 == id2:
                found_loop = True
                pnt = LL.head
                for _ in range(id1):
                    pnt = pnt.next
                LL.head = LL.tail = pnt
                print(f"Set node.next complete!, index:value = {id1}:{pnt.data} -> {id2}:{pnt.data}")
            else:
                pnt = LL.head
                pnt_to = LL.head
                if id2 <= LL.size - 1 and id1 > id2:
                    found_loop = True
                if id1 != 0:
                    for _ in range(id1):
                        pnt = pnt.next
                    before = pnt.data
                    for _ in range(id2):
                        pnt_to = pnt_to.next
                    pnt.next = pnt_to
                    print(f"Set node.next complete!, index:value = {id1}:{before} -> {id2}:{pnt_to.data}")
                else:
                    before = LL.head.data
                    for _ in range(id2):
                        pnt_to = pnt_to.next
                    LL.head.next = pnt_to
                    print(f"Set node.next complete!, index:value = 0:{before} -> {id2}:{pnt_to.data}")

if not found_loop:
    if LL.size != 0:
        print(f"No Loop\n{LL}")
    else:
        print("No Loop\nEmpty")
else:
    print("Found Loop")