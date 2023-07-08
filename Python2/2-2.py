def weirdSubtract(n, k):
    for i in range(k):
        try:
            if str(n)[-1] == '0':
                n = "".join(str(n)[0:len(str(n))-1])
                n = int(n)
            else:
                n -= 1
        except:
            return 0
    return n

n, s = input("Enter num and sub : ").split()
print(weirdSubtract(int(n), int(s)))
