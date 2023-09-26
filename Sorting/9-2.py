def straightsort(inp, outer, last_elem=-1):
    if outer == 1:
        return inp
    ssort = inp[:outer]
    if max(ssort) == inp[last_elem]:
        return straightsort(inp, outer-1, last_elem-1)
    else:
        p_last = inp[last_elem]
        p_max = max(ssort)
        inp[inp.index(max(ssort))], inp[last_elem] = inp[last_elem], inp[inp.index(max(ssort))]
        print(f"swap {p_last} <-> {p_max} : {inp}")
        return straightsort(inp, outer-1, last_elem-1)


inp = [int(i) for i in input("Enter Input : ").split(" ")]
straightsort(inp, len(inp))
print(inp)
