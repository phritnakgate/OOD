h, w = input("Enter your High and Weight : ").split()
bmi = float(w) / (float(h) * float(h))
if bmi >= 30:
    print("Fat")
elif 25 <= bmi < 30:
    print("Getting Fat")
elif 23 <= bmi < 25:
    print("More than Normal Weight")
elif 18.5 <= bmi < 23:
    print("Normal Weight")
else:
    print("Less Weight")