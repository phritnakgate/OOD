inp = input('Enter Input : ').split('/')
N = int(inp[0])
son = [int(i) for i in inp[1].split()]

# Check if value != [N / 2] + 1
if len(son) != N // 2 + 1:
    print("Incorrect Input")
    exit(0)

# Create Tree
L = [None] * (N + 1)

for i in range(N // 2 + 1, N + 1):
    L[i] = son[i - (N // 2 + 1)]

for i in range(N, 0, -1):
    if L[i] is None:
        m = min(L[2 * i], L[2 * i + 1])
        L[2 * i] -= m
        L[2 * i + 1] -= m
        L[i] = m

x = 0
for i in range(1, N + 1):
    x += L[i]

print(x)
