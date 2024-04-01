Weight = float(input("Weight: "))
unit = input("What weight did you select? (K)g or (L)bs: ")
K = (Weight * 0.4536)
L =  (Weight * 2.205)

if unit.upper() == "K":
    print('Weight in pounds: ',   L)
elif unit.upper() == "L":
    print('Weight in Kilograms: ',  K)
print("Conversion Complete")