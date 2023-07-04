print(" *** Divisible number *** ")
num = int(input("Enter a positive number : "))

if num <= 0:
    print(str(num) + " is OUT of range !!!")
else:
    divi = []
    if num == 1:
        print("Output ==> 1")
        print("Total ==> 1")
    else:
        divi.extend([1, num])
        i = 2
        while i != num:
            if num % i == 0 and int(i) not in divi:
                divi.insert(1, i)
                if int(i) not in divi:
                    divi.insert(1, num / i)
                i += 1
            else:
                i += 1
        divi.sort()
        l_num = ""
        for i in range(len(divi)):
            l_num += str(divi[i])
            l_num += " "
        print("Output ==> "+ l_num)
        print("Total ==> "+str(len(divi)))
