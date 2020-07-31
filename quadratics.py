import cmath
print("Input a, b, and c from a quadratic formula to solve for x. ")
a = float(input("a = "))
b = float(input("a = "))
c = float(input("c = "))
#quadratic formula: x = -b +- sqrt(b^2 + 4ac)/2a
d = (b**2) - (4*a*c)
sol1 = (-b + cmath.sqrt(d))/(2*a)
sol2 = (-b - cmath.sqrt(d))/(2*a)
solution1 = str(sol1)
solution2 = str(sol2)
final1 = solution1.replace("+0j", "")
final2 = solution2.replace("+0j", "")
print("The solutions are {0} and {1}" .format(final1, final2))