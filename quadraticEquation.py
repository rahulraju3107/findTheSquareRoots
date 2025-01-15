# Please write a program for solving a quadratic equation of the form ax²+bx+c. The program asks for values a, b and c. It should then use the quadratic formula to solve the equation.
# The quadratic formula expressed with the Python sqrt function is as follows:  x = (-b ± sqrt(b²-4ac))/(2a).
# You can assume the equation will always have two real roots, so the above formula will always work.
# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

from math import sqrt

a = float(input("Value of a:"))
b = float(input("Value of b:"))
c = float(input("Value of c:"))

#calculates the discriminant from the above quadratic formula
discriminant = b**2 - 4*a*c 

# to calculate the two roots
root1 = (-b + sqrt(discriminant)) / (2 * a)
root2 = (-b - sqrt(discriminant)) / (2 * a)

print(f"\nThe roots are {root1} and {root2}")

# NOTE1: the plus/minus from the above formula is how we get 2 different equations to solve for the 2 roots (one for + and one for -)
# NOTE2: the discriminant is the part of the formula under the square root symbol