print(" *** Divisible number *** ")
num = int(input("Enter a positive number : "))

if num <= 0:
    print(str(num) + " is OUT of range !!!")
else:
    result = [1, num]
    if num == 1:
        print("Output ==> 1")
        print("Total ==> 1")
    else:
        i = 2
        while i != num:
            if num % i == 0 and int(i) not in result:
                result.append(i)
                i += 1
            else:
                i += 1
        result.sort()
        l_num = ""
        for i in result:
            l_num += str(i)
            l_num += " "
        print("Output ==> "+ l_num)
        print("Total ==> "+str(len(result)))
