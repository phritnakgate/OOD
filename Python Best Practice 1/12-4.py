def rotate_string(fs, ls):
    rotated = []
    # First String
    f_rt = fs[-2] + fs[-1] + fs[0:len(fs) - 2]
    rotated.append(f_rt)
    # Last String
    l_rt = ls[3:len(ls) - 3] + ls[-3:] + ls[0:3]
    rotated.append(l_rt)
    return rotated


print("*** String Rotation ***")
inp = input("Enter 2 strings : ").split()
rotate = [rotate_string(inp[0], inp[1])]
runner = 0
while True:
    check = rotate[runner]
    if check == inp:
        rotate.append(inp)
        if len(rotate) > 6:
            print(" . . . . . ")
        print(str(len(rotate) - 1) + " " + inp[0] + " " + inp[1])
        print("Total of  " + str(len(rotate) - 1) + " rounds.")
        break
    else:
        rotate.append(rotate_string(check[0], check[1]))
        if len(rotate) <= 6:
            print(str(len(rotate) - 1) + " " + check[0] + " " + check[1])
        runner += 1
