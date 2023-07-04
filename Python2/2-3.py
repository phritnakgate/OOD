def odd_even(type, data, mode):
    if type == "L":
        l = [i for i in data.split(" ")]
        result = []
        if mode == "Odd":
            for i in range(0, len(l), 2):
                result.append(l[i])
            return result
        elif mode == "Even":
            for i in range(1, len(l), 2):
                result.append(l[i])
            return result
    elif type == "S":
        result = ""
        if mode == "Odd":
            for i in range(0, len(data), 2):
                result += data[i]
            return result
        elif mode == "Even":
            for i in range(1, len(data), 2):
                result += data[i]
            return result


print("*** Odd Even ***")
t, d, m = [items for items in input("Enter Input : ").split(",")]
print(odd_even(t, d, m))
