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


secret, hint = input("Enter code,hint : ").split(",")
secret_queue = Queue()

diff = ord(hint) - ord(secret[0])

for c in secret:
    secret_queue.enqueue(chr(ord(c)+diff))
    print(secret_queue.queue)
