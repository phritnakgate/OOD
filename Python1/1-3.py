def permute(l):
    if len(l) == 0:
        return []
    if len(l) == 1:
        return [l]

    result = [[]]
    for i in l:
        lst = []
        for j in result:
            for k in range(len(j) + 1):
                lst.append(j[:k] + [i] + j[k:])
                result = lst
    return result

print("*** Fun with permute ***")
inp = [int(e) for e in input("input : ").split(",")]
print("Original Cofllection: ", inp)
print("Collection of distinct numbers:")
print("", permute(inp))
