inp = [int(i) for i in input("Data : ").split(" ")]
result = [inp[0]]
print(f"1 : {result}")
lis = 1
for i in range(1, len(inp)):
    for j in range(len(result)):
        if inp[i] <= result[-1]:
            if len(result) == 1:
                result[-1] = inp[i]
            else:
                result.pop(-1)
        else:
            result.append(inp[i])
            if len(result) > lis:
                lis = len(result)
            break
    print(f"{i + 1} : {result}")

print(f"longest increasing subsequence : {lis}")
