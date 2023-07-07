class MyInt:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num

    def toRoman(self):
        result = ""
        if 6000 > self.__num > 0:
            if int(self.__num / 1000) != 0:
                result += "M" * int(self.__num / 1000)
                self.__num -= 1000 * int(self.__num / 1000)
            if int(self.__num / 900) != 0:
                result += "CM"
                self.__num -= 900
            if int(self.__num / 100) != 0:
                if int(self.__num / 100) > 5:
                    result += "D"
                    self.__num -= 500
                    result += "C" * int(self.__num / 100)
                    self.__num -= 100 * int(self.__num / 100)
                elif int(self.__num / 100) == 5:
                    result += "D"
                    self.__num -= 500
                elif int(self.__num / 100) == 4:
                    result += "CD"
                    self.__num -= 400
                else:
                    result += "C" * int(self.__num / 100)
                    self.__num -= 100 * int(self.__num / 100)
            if int(self.__num / 90) != 0:
                result += "XC"
                self.__num -= 90
            if int(self.__num / 10) != 0:
                if int(self.__num / 10) > 5:
                    result += "L"
                    self.__num -= 50
                    result += "X" * int(self.__num / 10)
                    self.__num -= 10 * int(self.__num / 10)
                elif int(self.__num / 10) == 5:
                    result += "L"
                    self.__num -= 50
                elif int(self.__num / 10) == 4:
                    result += "XL"
                    self.__num -= 40
                else:
                    result += "X" * int(self.__num / 10)
                    self.__num -= 10 * int(self.__num / 10)
            if self.__num == 9:
                result += "IX"
            if 9 > self.__num > 5:
                result += "V"
                self.__num -= 5
                result += "I" * self.__num
                self.__num -= self.__num
            if self.__num == 5:
                result += "V"
                self.__num -= 5
            if self.__num == 4:
                result += "IV"
            if 0 < self.__num < 4:
                result += "I" * self.__num
            return result
        else:
            return ""

    def __add__(self, other):
        return MyInt(self.__num + other.get_num() + int((self.__num + other.get_num())/2))


print(" *** class MyInt ***")
inp = [int(i) for i in input("Enter 2 number : ").split()]
a = MyInt(inp[0])
b = MyInt(inp[1])
c = a + b

print(str(inp[0]) + " convert to Roman : " + a.toRoman())
print(str(inp[1]) + " convert to Roman : " + b.toRoman())
print(str(inp[0]) + " + " + str(inp[1]) + " = " + str(c.get_num()))
