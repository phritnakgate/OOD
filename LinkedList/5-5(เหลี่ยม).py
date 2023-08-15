class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, head=None):
        if head is None:
            self.head = None
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
            st += " "
            st += str(t)
        return st

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def append(self, data):
        p = Node(data)
        if self.head is None:
            self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
        self.size += 1


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

    def __len__(self):
        return len(self.queue)

    def __str__(self):
        return ' '.join(str(i) for i in self.queue)


def createLL(LL):
    l = LinkedList()
    for i in LL:
        l.append(i)
    return l


def printLL(head):
    st = str(head)
    t = head
    while t.next is not None:
        t = t.next
        st += " "
        st += str(t)
    return st


def SIZE(head):
    return head.size


def scarmble(head, b, r, size):
    bott = bottomup(head, int((b / 100) * size))
    print(f"BottomUp {b:.3f} % : {bott}")
    rif = riffle(bott, int((r / 100) * size))
    print(f"Riffle {r:.3f} % : {rif}")
    derif = deriffle(rif, int((r / 100) * size), size)
    print(f"Deriffle {r:.3f} % : {bott}")
    debott = debottomup(bott, int((b / 100) * size), size)
    print(f"Debottomup {b:.3f} % : {debott}")
    return debott


def bottomup(head, b):
    q = Queue()
    cur = head.head

    for _ in range(round(b)):
        q.enqueue(cur.value)
        cur = cur.next
    new_ll = LinkedList(cur)
    while not q.is_empty():
        new_ll.append(q.dequeue())

    return new_ll


def riffle(head, r):
    q1 = Queue()
    q2 = Queue()
    cur = head.head
    if r == 1:
        return head
    for _ in range(round(r)):
        q1.enqueue(cur.value)
        cur = cur.next
    while cur is not None:
        q2.enqueue(cur.value)
        cur = cur.next
    new_ll = LinkedList()
    while not q1.is_empty() and not q2.is_empty():
        new_ll.append(q1.dequeue())
        new_ll.append(q2.dequeue())
    if q2.is_empty():
        if not q1.is_empty():
            while not q1.is_empty():
                new_ll.append(q1.dequeue())
    if q1.is_empty():
        if not q2.is_empty():
            while not q2.is_empty():
                new_ll.append(q2.dequeue())

    return new_ll


def debottomup(head, b, size):

    q = Queue()
    b = size - round(b)
    cur = head.head
    for _ in range(b):
        q.enqueue(cur.value)
        cur = cur.next
    new_ll = LinkedList(cur)
    while not q.is_empty():
        new_ll.append(q.dequeue())

    return new_ll


def deriffle(head, r, size):
    new_ll = LinkedList()
    q1 = Queue()
    q2 = Queue()
    cur = head.head
    eiei = round(r)
    r = size - round(r)
    if r == size - 1:
        return head

    if r >= 5:
        ind = 0
        while len(q2) != r:
            if ind % 2 == 0:
                if cur.next is not None:
                    q1.enqueue(cur.value)
                    cur = cur.next
                    ind += 1
                else:
                    break
            else:
                if cur.next is not None:
                    q2.enqueue(cur.value)
                    cur = cur.next
                    ind += 1
                else:
                    break
    else:
        ind = 0
        while len(q2) != eiei:
            if ind % 2 == 0:
                if cur.next is not None:
                    q1.enqueue(cur.value)
                    cur = cur.next
                    ind += 1
                else:
                    break
            else:
                if cur.next is not None:
                    q2.enqueue(cur.value)
                    cur = cur.next
                    ind += 1
                else:
                    break
    if cur is not None:
        while cur is not None:
            q1.enqueue(cur.value)
            cur = cur.next
    while not q1.is_empty():
        new_ll.append(q1.dequeue())
    while not q2.is_empty():
        new_ll.append(q2.dequeue())
    #print(f"Cur:{cur}")
    #print(f"Q1:{q1}")
    #print(f"Q2:{q2}")
    return new_ll

inp1, inp2 = input('Enter Input : ').split('/')
print('-' * 50)
h = createLL(inp1.split())
for i in inp2.split('|'):
    print("Start : {0}".format(printLL(h.head)))
    k = i.split(',')
    if k[0][0] == "B" and k[1][0] == "R":
        h = scarmble(h, float(k[0][2:]), float(k[1][2:]), SIZE(h))
    elif k[0][0] == "R" and k[1][0] == "B":
        h = scarmble(h, float(k[1][2:]), float(k[0][2:]), SIZE(h))
    print('-' * 50)
