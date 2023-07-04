print(" *** String count *** ")
message = str(input("Enter message : "))
upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
tt_upper = 0
tt_lower = 0
uni_upper = ""
uni_lower = ""
for i in range(len(message)):
    if message[i] in upper_char:
        tt_upper += 1
        if message[i] not in uni_upper:
            uni_upper += message[i]
    if message[i] in lower_char:
        tt_lower += 1
        if message[i] not in uni_lower:
            uni_lower += message[i]
s_u = "".join(sorted(uni_upper))
s_l = "".join(sorted(uni_lower))
uni_upper = ""
uni_lower = ""
for j in range(len(s_u)):
    uni_upper += s_u[j]
    uni_upper += "  "
for k in range(len(s_l)):
    uni_lower += s_l[k]
    uni_lower += "  "
print("No. of Upper case characters : " + str(tt_upper))
print("Unique Upper case characters : " + uni_upper)
print("No. of Lower case Characters : " + str(tt_lower))
print("Unique Lower case characters : " + uni_lower)
