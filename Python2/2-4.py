def threesum(lst, length):
    zerosum = []
    lst.sort()

    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if lst[i] + lst[j] + lst[k] == 0:
                    zerosum.append([lst[i], lst[j], lst[k]])

    return zerosum


inp = [int(i) for i in input("Enter Your List : ").split()]
l = len(inp)
zero = [0 for _ in range(l)]
if l <= 2:
    print("Array Input Length Must More Than 2")
elif inp == zero:
    print([[0, 0, 0]])
else:
    print(threesum(inp, l))
