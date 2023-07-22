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


width, height, room = input("Enter width, height, and room: ").split()
width, height = int(width), int(height)

room_data = [sprite for sprite in room.split(",")]
walking = Queue()
log = []

is_f = False

# Check Error
if len(room_data) != height:
    print("Invalid map input.")
    exit(0)
for element in room_data:
    if len(element) != width:
        print("Invalid map input.")
        exit(0)
    if "F" in element:
        is_f = True

if not is_f:
    print("Invalid map input.")

# Find Starting Point
for i in range(len(room_data)):
    for j in range(len(room_data[i])):
        if room_data[i][j] == "F":
            walking.enqueue((j, i))
            print("Queue:", walking.queue)
            break

# Walking
while True:
    try:
        dq = walking.dequeue()
        # North
        if len(room_data) - 1 >= dq[1] - 1 >= 0:
            if room_data[dq[1] - 1][dq[0]] == "_":
                if (dq[0], dq[1] - 1) not in log:
                    walking.enqueue((dq[0], dq[1] - 1))
                    log.append((dq[0], dq[1] - 1))
            elif room_data[dq[1] - 1][dq[0]] == "O":
                print("Found the exit portal.")
                exit(0)
        # East
        if len(room_data[dq[1]]) - 1 >= dq[0] + 1 >= 0:
            if room_data[dq[1]][dq[0] + 1] == "_":
                if (dq[0] + 1, dq[1]) not in log:
                    walking.enqueue((dq[0] + 1, dq[1]))
                    log.append((dq[0] + 1, dq[1]))
            elif room_data[dq[1]][dq[0] + 1] == "O":
                print("Found the exit portal.")
                exit(0)

        # South
        if len(room_data) - 1 >= dq[1] + 1 >= 0:
            if room_data[dq[1] + 1][dq[0]] == "_":
                if (dq[0], dq[1] + 1) not in log:
                    walking.enqueue((dq[0], dq[1] + 1))
                    log.append((dq[0], dq[1] + 1))
            elif room_data[dq[1] + 1][dq[0]] == "O":
                print("Found the exit portal.")
                exit(0)
        # West
        if len(room_data[dq[1]]) - 1 >= dq[0] - 1 >= 0:
            if room_data[dq[1]][dq[0] - 1] == "_":
                if (dq[0] - 1, dq[1]) not in log:
                    walking.enqueue((dq[0] - 1, dq[1]))
                    log.append((dq[0] - 1, dq[1]))
            elif room_data[dq[1]][dq[0] - 1] == "O":
                print("Found the exit portal.")
                exit(0)
        if not walking.queue:
            print("Cannot reach the exit portal.")
            exit(0)
        print("Queue:", walking.queue)
    except IndexError:
        print("Cannot reach the exit portal.")
        exit(0)
