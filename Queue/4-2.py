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


# Input Zone
people, time = input("Enter people and time : ").split()
time = int(time)

# Queue Zone
main_row = Queue()
r1 = Queue()
r2 = Queue()

# Add people to main queue
for p in people:
    main_row.enqueue(p)

# Paying Zone
time1, time2 = 1, 0
while time1 <= time:
    # Set time stamp of r2
    if not r2.queue:
        time2 = 0

    if main_row:
        if r1.__len__() < 5:
            if time1 % 3 == 1 and time1 != 1:
                r1.enqueue(main_row.dequeue())
                r1.dequeue()
                print(time1, main_row.queue, r1.queue, r2.queue)
            else:
                r1.enqueue(main_row.dequeue())
                print(time1, main_row.queue, r1.queue, r2.queue)
        else:
            if time1 % 3 == 1:
                r1.enqueue(main_row.dequeue())
                r1.dequeue()
                if time2 % 2 == 0 and time2 != 1:
                    r2.dequeue()
                    time2 += 1
                    print(time1, main_row.queue, r1.queue, r2.queue)

                elif not r2.is_empty():
                    time2 += 1
                    print(time1, main_row.queue, r1.queue, r2.queue)
                else:
                    print(time1, main_row.queue, r1.queue, r2.queue)
            else:
                if time2 % 2 == 0 and time2 != 1:
                    r2.dequeue()
                    r2.enqueue(main_row.dequeue())
                    time2 += 1
                    print(time1, main_row.queue, r1.queue, r2.queue)
                else:
                    r2.enqueue(main_row.dequeue())
                    print(time1, main_row.queue, r1.queue, r2.queue)
                    time2 += 1

    # Main Queue Cleared
    else:
        # r1
        if time1 % 3 == 1 and not r1.is_empty():
            r1.dequeue()
            print(time1, main_row.queue, r1.queue, r2.queue)
            if not r2.is_empty():
                time2 += 1
        else:
            # r2
            if time2 % 2 == 0 and not r2.is_empty():
                r2.dequeue()
                time2 += 1
                print(time1, main_row.queue, r1.queue, r2.queue)
            else:
                print(time1, main_row.queue, r1.queue, r2.queue)
                if time2 != 0:
                    time2 += 1

    time1 += 1