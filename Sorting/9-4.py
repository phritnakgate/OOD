def bubblesort(data, outer=0, inner=0):
    if len(data) == 1:
        return data
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

def find_median(data):
    if len(data) == 1:
        return data[0]
    elif len(data) == 2:
        return (data[0] + data[1]) / 2
    else:
        if len(data) % 2 != 0:
            return data[len(data) // 2]
        else:
            return (data[len(data) // 2] + data[len(data) // 2 - 1]) / 2
l = [int(e) for e in input("Enter Input : ").split()]
fmed = []
fmed_display = []
for i in l:
    fmed.append(i)
    fmed_display.append(i)
    bubblesort(fmed)
    print(f"list = {fmed_display} : median = {float(find_median(fmed))}")
