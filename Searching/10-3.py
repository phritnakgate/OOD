inp = int(input("simple sqrt: "))
low = 1
high = 2
while True:
    lowsq = low ** 2
    highsq = high ** 2
    if lowsq <= inp < highsq:
        print(low)
        break
    else:
        low += 1
        high += 1
