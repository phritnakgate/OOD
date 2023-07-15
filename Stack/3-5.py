class Stack:
    def __init__(self, ls=None):
        if ls is None:
            self.stack = []
        else:
            self.stack = ls

    # Push
    def push(self, i):
        self.stack.append(i)

    # Pop
    def pop(self):
        return self.stack.pop()

    # Peek
    def peek(self):
        return self.stack[-1]

    # isEmpty
    def isEmpty(self):
        if not self.stack:
            return False
        else:
            return True

    # Size
    def size(self):
        return len(self.stack)


def parking(maxcar, insoi, command, regis):
    soi1 = Stack()
    soi2 = Stack()

    if insoi == "0":  # Check if no car in soi
        if command == "depart":
            print(f"car {regis} cannot depart : Soi Empty\n{soi1.stack}")
        elif command == "arrive":
            soi1.push(regis)
            print(f"car {regis} arrive! : Add Car {regis}\n{soi1.stack}")
    else:
        soicar = [c for c in insoi.split(",")]
        for sc in soicar:
            soi1.push(int(sc))

        # Arrival
        if command == "arrive":
            if soi1.size() >= maxcar:
                print(f"car {regis} cannot arrive : Soi Full\n{soi1.stack}")
            else:
                isin = False
                # Check if regis of car is already in soi
                for i in range(soi1.size()):
                    if soi1.peek() == regis:
                        isin = True
                        break
                    else:
                        soi2.push(soi1.pop())
                for j in range(soi2.size()):
                    soi1.push(soi2.peek())
                    soi2.pop()
                if isin:
                    print(f"car {regis} already in soi\n{soi1.stack}")
                else:
                    soi1.push(regis)
                    print(f"car {regis} arrive! : Add Car {regis}\n{soi1.stack}")
        # Departure
        elif command == "depart":
            rmv_stat = False
            # Check if regis of car is already in soi
            for i in range(soi1.size()):
                if soi1.peek() == regis:
                    soi1.pop()
                    rmv_stat = True
                    break
                else:
                    soi2.push(soi1.pop())
            for j in range(soi2.size()):
                soi1.push(soi2.peek())
                soi2.pop()
            if rmv_stat:
                print(f"car {regis} depart ! : Car {regis} was remove\n{soi1.stack}")
            else:
                print(f"car {regis} cannot depart : Dont Have Car {regis}\n{soi1.stack}")


print("******** Parking Lot ********")
m, s, o, n = input("Enter max of car,car in soi,operation : ").split()
m, n = int(m), int(n)

parking(m, s, o, n)
