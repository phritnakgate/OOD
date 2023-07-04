print("*** Fun with countdown ***")
l = [int(items) for items in input("Enter List : ").split()]
cnt_dn = []
answer = []
i, k = 0, 0
while i < len(l):
    if l[i] == 1:
        cnt_dn.append([1])
        i += 1
    else:
        try:
            if l[i] == 1:
                cnt_dn.append([1])
                i += 1
            else:
                if l[i] - 1 != l[i+1]:
                    i += 1
                    continue
                else:
                    checker = []
                    for j in range(1, l[i]+1):
                        checker.append(j)
                    checker.reverse()
                    tes = []
                    for k in range(len(checker)):
                        tes.append(l[i+k])
                    if checker == tes:
                        cnt_dn.append(tes)
                        i = i+k+1
        except:
            break
answer = [len(cnt_dn), cnt_dn]
print(answer)