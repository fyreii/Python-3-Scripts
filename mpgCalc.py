m = int(input("Please enter the number of miles driven: "))
g = int(input("Please enter the number of gallons used: "))
mpg = m / g
print("The approximate MPG for this trip is " + str(round(mpg, 2)) + ".")