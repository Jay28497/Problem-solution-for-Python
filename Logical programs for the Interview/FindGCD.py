# GCD (Greatest common divisor)
import math

a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
print("GCD is: ", math.gcd(a, b))


########
#  OR  #
########

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))
GCD = gcd(a, b)
print("GCD is: ", GCD)
