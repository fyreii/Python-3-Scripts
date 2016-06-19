P = 10000
n = 12
r = 0.08
t = int(input("Please enter the number of years to calculate interest: "))
A = P * (1.0 + r/n) ** n * t

# This method below is the "proper" method using .format
print("The amount compounded after {0} years will be {1}".format(int(t), int(A)))

# This method is what the school ActiveCode accepted as 'correct' with rounding cause blah digits
print("The amount compounded after " + str(t) + " years will be " + str(round(A,2)) + ".")