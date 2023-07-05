class FunString:

    def __init__(self, string):
        self.__string = string
        self.__upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.__lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __str__(self):
        pass

    def size(self):
        return len(self.__string)

    def change_size(self):
        ch_size = ""
        for i in range(len(self.__string)):
            if self.__string[i] in self.__upper_char:
                ch_size += self.__lower_char[self.__upper_char.index(self.__string[i])]
            elif self.__string[i] in self.__lower_char:
                ch_size += self.__upper_char[self.__lower_char.index(self.__string[i])]
        return ch_size

    def reverse(self):
        rev = ""
        i = len(self.__string) - 1
        while i >= 0:
            rev += self.__string[i]
            i -= 1
        return rev

    def delete_same(self):
        ds = ""
        uniq = []
        for i in self.__string:
            if i not in uniq:
                uniq.append(i)
                ds += i
        return ds

str1, str2 = input("Enter String and Number of Function : ").split()

res = FunString(str1)

if str2 == "1":
    print(res.size())

elif str2 == "2":
    print(res.change_size())

elif str2 == "3":
    print(res.reverse())

elif str2 == "4":
    print(res.delete_same())
