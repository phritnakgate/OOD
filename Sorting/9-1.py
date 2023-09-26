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


inp = [int(i) for i in input("Enter Input : ").split(" ")]
bubblesort(inp)
print(inp)
