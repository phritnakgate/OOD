def palindrome(st):
    if len(st) == 1:
        return True
    elif len(st) == 2:
        if st[1] == st[0]:
            return True
        else:
            return False
    else:
        if pchecker(st, 0, len(st) - 1):
            return True
        else:
            return False


def pchecker(st, f, b):
    if st[f] != st[b]:
        return False
    if f < b:
        return pchecker(st, f + 1, b - 1)
    return True


s = str(input("Enter Input : "))
if palindrome(s):
    print(f"'{s}' is palindrome")
else:
    print(f"'{s}' is not palindrome")
