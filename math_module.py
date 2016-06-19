import math

# part 1 - pythagorean theorem

side1 = 3
side2 = 4
hypotenuse = math.hypot(side1,side2)
print(hypotenuse)

# part2 - pi and approx pi

pi = 2 * (math.asin(math.sqrt(1 - 1**2)) + abs(math.asin(1)))
print("The approximate pi is: " + str(pi))
print("The module pi is: " + str(math.pi))

