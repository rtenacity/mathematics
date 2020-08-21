import cmath
print("Derivative solver.")
a = int(input("constant = "))
b = input("variable = ")
c = float(input("power = "))

print("The formula is " + str(a*c) + str(b) + "^" + str(c-1))

d = c - 1.0

e = a*c

f = float(input("x = "))

g = f**d

h = g*e

print(str(b)+ " = " + str(h))


