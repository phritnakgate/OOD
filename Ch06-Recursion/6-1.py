def factorial(f):
    if f in [0, 1]:
        return 1
    else:
        return f * factorial(f-1)


num = int(input("Enter Number : "))
print(f"{num}! = {factorial(num)}")
