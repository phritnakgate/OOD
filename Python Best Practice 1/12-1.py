print(" *** Wind classification *** ")
wind = float(input("Enter wind speed (km/h) : "))
if 0 <= wind < 52:
    print("Wind classification is Breeze.")
elif 52 <= wind < 56:
    print("Wind classification is Depression.")
elif 56 <= wind < 102:
    print("Wind classification is Tropical Storm.")
elif 102 <= wind < 209:
    print("Wind classification is Typhoon.")
elif wind >= 209:
    print("Wind classification is Super Typhoon.")
else:
    print("!!!Wrong value can't classify.")
