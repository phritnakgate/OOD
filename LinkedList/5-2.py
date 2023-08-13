class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next is not None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        # print(f"Tail is {self.tail.value}")
        if self.isEmpty():
            return "Empty"
        if self.tail is None:
            cur, s = self.head, str(self.head.value) + " "
        else:
            cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous is not None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head is None

    def append(self, item):
        p = Node(item)
        if self.head is None:
            self.tail = self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
            self.tail = p
            p.previous = t
        self.size += 1

    def addHead(self, item):
        p = Node(item)
        if self.head is None:
            self.tail = self.head = p
        else:
            p.next = self.head
            self.head.previous = p
            self.head = p
        self.size += 1

    def insert(self, pos, item):
        new_node = Node(item)
        if self.isEmpty():
            self.head = self.tail = new_node
            self.size += 1
        elif pos == 0 and self.size != 0:
            self.addHead(item)
        elif pos < 0:
            current = self.tail
            prev = None
            current_index = 0
            if -pos >= self.size:
                current = self.head
                self.head = new_node
                new_node.next = current
                current.previous = new_node
            else:
                while current_index != pos:
                    prev = current
                    current = current.previous
                    current_index -= 1
                current.next = new_node
                prev.previous = new_node
                new_node.previous = current
                new_node.next = prev
            self.size += 1
        else:
            current = self.head
            prev = None
            current_index = 0
            if pos >= self.size:
                current = self.tail
                self.tail = new_node
                new_node.previous = current
                current.next = new_node
            else:
                while current is not None and current_index < pos:
                    prev = current
                    current = current.next
                    current_index += 1
                if current is None:
                    prev.next = new_node
                else:
                    # Insert the new node between prev and current
                    prev.next = new_node
                    new_node.previous = prev
                    new_node.next = current
                    current.previous = new_node
            self.size += 1

    def search(self, item):
        current = self.head
        pos = 0
        while current is not None:
            if current.value == item:
                return 'Found'
            current = current.next
            pos += 1
        return 'Not Found'

    def index(self, item):
        if self.head is not None:
            t = self.head
            ind = 0
            if t.value == item:
                return ind
            else:
                while t.next is not None:
                    if t.value == item:
                        return ind
                    t = t.next
                    ind += 1
                return -1
        else:
            return -1


    def size(self):
        return self.size

    def pop(self, pos):
        if self.isEmpty():
            return "Out of Range"
        else:
            if pos > self.size - 1:
                return "Out of Range"
            else:
                if self.size == 1:
                    self.head = None
                    self.size -= 1
                    return "Success"
                elif pos == self.size - 1:
                    prv = self.tail.previous
                    self.tail = prv
                    self.tail.next = None
                    self.size -= 1
                    return "Success"
                else:
                    current = self.head
                    for _ in range(pos):
                        current = current.next
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    self.size -= 1
                    return "Success"



L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size, L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])

print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
