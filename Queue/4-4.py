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


print(" ***Cafe***")
inp = input("Log : ").split("/")

b1_status, b2_status = Queue(), Queue()
now, avail1, avail2 = 0, 0, 0
log_id, log_wait = [], []

for i in range(1, len(inp)+1):
    wait = 0
    entrance, coffee = inp[i-1].split(",")
    entrance, coffee = int(entrance), int(coffee)
    log_id.append(i)

    now = entrance
    if not b1_status:
        avail1 = now + wait + coffee
        b1_status.enqueue([i, avail1])
        log_wait.append(wait)
    elif not b2_status:
        avail2 = now + wait + coffee
        b2_status.enqueue([i, avail2])
        log_wait.append(wait)
    else:
        if avail1 <= now < avail2:
            avail1 = now + wait + coffee
            b1_status.enqueue([i, avail1])
            log_wait.append(wait)
        elif avail1 > now >= avail2:
            avail2 = now + wait + coffee
            b2_status.enqueue([i, avail2])
            log_wait.append(wait)
        elif now >= avail1 and now >= avail2:
            while b1_status:
                dq = b1_status.dequeue()
                print(f"Time {dq[1]} customer {dq[0]} get coffee")
            avail1 = now + wait + coffee
            b1_status.enqueue([i, avail1])
            log_wait.append(wait)
            while b2_status:
                dq = b2_status.dequeue()
                print(f"Time {dq[1]} customer {dq[0]} get coffee")
        else:
            if avail1 - now < avail2 - now:
                wait = avail1 - now
                avail1 = now + wait + coffee
                b1_status.enqueue([i, avail1])
                log_wait.append(wait)
            elif avail2 - now < avail1 - now:
                wait = avail2 - now
                avail2 = now + wait + coffee
                b2_status.enqueue([i, avail2])
                log_wait.append(wait)
            else:
                if b1_status.__len__() > b2_status.__len__():
                    wait = avail2 - now
                    avail2 = now + wait + coffee
                    b2_status.enqueue([i, avail2])
                    log_wait.append(wait)
                else:
                    wait = avail1 - now
                    avail1 = now + wait + coffee
                    b1_status.enqueue([i, avail1])
                    log_wait.append(wait)

remaining = []
while b1_status:
    remaining.append(b1_status.dequeue())
while b2_status:
    remaining.append(b2_status.dequeue())

#print(remaining)
remaining_sorted = sorted(remaining, key=lambda x: (x[1], x[0]))
for i in remaining_sorted:
    print(f"Time {i[1]} customer {i[0]} get coffee")

if max(log_wait) != 0:
    ind = log_wait.index(max(log_wait))
    print(f"The customer who waited the longest is : {log_id[ind]}\nThe customer waited for {max(log_wait)} minutes")
else:
    print("No waiting")
