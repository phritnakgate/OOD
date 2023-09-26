def bubblesort(data, outer=0, inner=0):
    # Check if checked all position
    if inner == len(data) - 1 - outer:
        if len(data) - 1 - outer == 1:
            return data
        else:
            return bubblesort(data, outer + 1, 0)

    if data[inner] > data[inner+1]:
        data[inner], data[inner+1] = data[inner+1], data[inner]
        return bubblesort(data, outer, inner + 1)
    else:
        return bubblesort(data, outer, inner + 1)

def bubblesortinv(data):
    for last in range(len(data)-1,0,-1):
        swaped = False
        for i in range(last):
            if data[i] < data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swaped = True
        if not swaped:
            break
def checkRep(inp):
    isRep = True
    for i in range(len(inp) - 1):
        if inp[i] != inp[i + 1]:
            isRep = not isRep
            break
    if isRep:
        return True
    return False

def sthDrome(inp, ssort, ssort2):
    rep = checkRep(inp)
    if rep:
        print("Repdrome")
        return
    bubblesort(ssort)
    bubblesortinv(ssort2)
    if inp == ssort:
        checker = set()
        for i in inp:
            checker.add(i)
        if list(checker) == inp:
            print("Metadrome")
        else:
            print("Plaindrome")
    elif inp == ssort2:
        checker = set()
        for i in inp:
            checker.add(i)
        checker = list(checker)
        bubblesortinv(checker)
        if checker == inp:
            print("Katadrome")
        else:
            print("Nialpdrome")
    else:
        print("Nondrome")



inp = [int(i) for i in input("Enter Input : ")]
ssort = inp.copy()
ssort2 = inp.copy()
sthDrome(inp, ssort, ssort2)
