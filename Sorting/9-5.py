def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


inp = [int(x) for x in input('input : ').split()]
pair = []
for i in range(0, len(inp) - 1, 2):
    co = (inp[i], inp[i+1])
    pair.append(co)

mergeSort(pair)
total_sum = 0
for i in range(1, len(pair)):
    for j in range(i - 1, -1, -1):
        if pair[i][0] > pair[j][0] and pair[i][1] < pair[j][1]:
            total_sum += pair[i][0]
            total_sum += pair[j][0]

print("ans =", total_sum)