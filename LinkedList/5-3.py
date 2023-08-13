class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)


def createList(l=[]):
    if l:
        tail = head = Node(l[0])
        if len(l) == 1:
            return head
        else:
            for i in range(1, len(l)):
                n = Node(l[i])
                tail.next = n
                tail = n
        return head


def printList(H):
    print(H, end=' ')
    t = H
    while t.next is not None:
        t = t.next
        print(t, end=' ')


def mergeOrderesList(p, q):
    od = current_od = Node(None)
    while p and q:
        if p.data < q.data:
            current_od.next = p
            p = p.next
        else:
            current_od.next = q
            q = q.next
        current_od = current_od.next

    while p:
        current_od.next = p
        p = p.next
        current_od = current_od.next

    while q:
        current_od.next = q
        q = q.next
        current_od = current_od.next

    return od.next


#################### FIX comand ####################
# input only a number save in L1,L2
inp = input("Enter 2 Lists : ").split(" ")
L1 = [int(l1) for l1 in inp[0].split(",")]
L2 = [int(l2) for l2 in inp[1].split(",")]
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ', end='')
printList(LL1)
print('\nLL2 : ', end='')
printList(LL2)
m = mergeOrderesList(LL1, LL2)
print('\nMerge Result : ', end='')
printList(m)
