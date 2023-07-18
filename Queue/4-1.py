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


myQueue = Queue()
inp = input("Enter Input : ").split(",")

# Command
for i in inp:
    if "E" in i:
        myQueue.enqueue(int(i.split()[1]))
        print(myQueue.__len__())
    elif "D" in i and not myQueue.is_empty():
        print(myQueue.queue[0], myQueue.queue.index(myQueue.queue[0]))
        myQueue.dequeue()
    elif "D" in i and myQueue.is_empty():
        print(-1)

# Final Queue
if myQueue.is_empty():
    print("Empty")
else:
    print(' '.join(str(i) for i in myQueue.queue))
