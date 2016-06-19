"""

Teresa Henderson
CST 100 - Bansal
05/15/2016

assign1.py

Part 1: Calculates the Celsius equivalent of a user input in F
Part 2: Calculates area of trapezoid based on user input

5/20/2016 - fixed lack of comments and variable names

"""

# provides user information on first calculator
print("Assignment Part I - Fahrenheit to Celsius \n")

# takes input as integer the temperature to be converted
userTemp = int(input("Please enter a temperature in degrees Fahrenheit: "))
# calculates the Celcius equivalent with the standard formula
inCelsius = 5.0/9.0 * (userTemp - 32)
# prints the converted temperature, restricting answer to two decimal places
print("The temperature in Celsius is: %.2f" % inCelsius + "\n")

# provides user information on second calculator
print("Assignment Part II - Area of Trapezoid \n")

# takes input as integer for height of trapezoid
height = int(input("Please enter the height of a trapezoid: "))
# takes input as integer for top length of trapezoid
top_length = int(input("Please enter the length of the bottom of the trapezoid: "))
# takes input as integer for bottom length of trapezoid
bottom_length = int(input("Please enter the length of the top of the trapezoid: "))
# calculates area of trapezoid using standard formula
Area = (top_length + bottom_length) / 2 * height
# output the area of the trapezoid with the given dimensions.
print("The area of the trapezoid with dimensions " + str(top_length) + " x " + str(bottom_length) + " is  " + str(Area) + ".")


