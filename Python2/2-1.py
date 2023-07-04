class Translator:

    def deci_to_roman(self, num):
        result = ""
        if 4000 > num > 0:
            if int(num / 1000) != 0:
                result += "M" * int(num / 1000)
                num -= 1000 * int(num / 1000)
            if int(num / 900) != 0:
                result += "CM"
                num -= 900
            if int(num / 100) != 0:
                if int(num / 100) > 5:
                    result += "D"
                    num -= 500
                    result += "C" * int(num / 100)
                    num -= 100 * int(num / 100)
                elif int(num / 100) == 5:
                    result += "D"
                    num -= 500
                elif int(num / 100) == 4:
                    result += "CD"
                    num -= 400
                else:
                    result += "C" * int(num / 100)
                    num -= 100 * int(num / 100)
            if int(num / 90) != 0:
                result += "XC"
                num -= 90
            if int(num / 10) != 0:
                if int(num / 10) > 5:
                    result += "L"
                    num -= 50
                    result += "X" * int(num / 10)
                    num -= 10 * int(num / 10)
                elif int(num / 10) == 5:
                    result += "L"
                    num -= 50
                elif int(num / 10) == 4:
                    result += "XL"
                    num -= 40
                else:
                    result += "X" * int(num / 10)
                    num -= 10 * int(num / 10)
            if num == 9:
                result += "IX"
            if 9 > num > 5:
                result += "V"
                num -= 5
                result += "I" * num
                num -= num
            if num == 5:
                result += "V"
                num -= 5
            if num == 4:
                result += "IV"
            if 0 < num < 4:
                result += "I" * num
            return result
        else:
            return ""

    def roman_to_deci(self, s):
        result = 0
        if s == "":
            return ""
        if len(s) == 1:
            if s == "I":
                return 1
            elif s == "V":
                return 5
            elif s == "X":
                return 10
            elif s == "L":
                return 50
            elif s == "C":
                return 100
            elif s == "D":
                return 500
            elif s == "M":
                return 1000
        else:
            i = 0
            while i <= len(s):
                try:
                    if s[i] == "M":
                        result += 1000
                    if s[i] == "D":
                        result += 500
                    if s[i] == "C":
                        if s[i + 1] == "M":
                            result += 900
                            i += 2
                        elif s[i + 1] == "D":
                            result += 400
                            i += 2
                        else:
                            result += 100
                    if s[i] == "L":
                        result += 50
                    if s[i] == "X":
                        if s[i + 1] == "C":
                            result += 90
                            i += 2
                        elif s[i + 1] == "L":
                            result += 40
                            i += 2
                        else:
                            result += 10
                    if s[i] == "V":
                        result += 5
                    if s[i] == "I":
                        if i == len(s) - 1:
                            result += 1
                        else:
                            if s[i + 1] == "X":
                                result += 9
                                break
                            elif s[i + 1] == "V":
                                result += 4
                                break
                            else:
                                result += 1
                    i += 1
                except:
                    break
        return result


num = int(input("Enter number to translate : "))

print(Translator().deci_to_roman(num))
print(Translator().roman_to_deci(Translator().deci_to_roman(num)))
