class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next == None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self, head=None):
        if head == None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next != None:  # Locating tail + finding size
                t = t.next
                self.size += 1
            self.tail = t

    def __str__(self):
        st = str(self.head)
        t = self.head
        while t.next != None:
            t = t.next
            st += "->"
            st += str(t)
        return "link list : " + st

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.size += 1

    def insert(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev = None
            current_index = 0
            while current is not None and current_index < index:
                prev = current
                current = current.next
                current_index += 1
            if current is None:
                prev.next = new_node
            else:
                # Insert the new node between prev and current
                prev.next = new_node
                new_node.next = current
        self.size += 1


inp = input("Enter Input : ").split(",")
l = LinkedList()
for i in inp:
    if ":" in i:
        comm = [int(x) for x in i.split(":")]
        try:
            if comm[0] > l.size:
                if l.size != 0:
                    print(f"Data cannot be added\n{l}")
                else:
                    print("Data cannot be added\nList is empty")
            else:
                l.insert(comm[0], comm[1])
                print(f"index = {comm[0]} and data = {comm[1]}")
                print(l)
        except:
            print(f"Data cannot be added\n{l}")
    else:
        if i == "" or i == " ":
            print("List is empty")
        else:
            for j in [int(x) for x in i.split(" ")]:
                l.append(j)
            print(l)
