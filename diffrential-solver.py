import cmath
print("Integral solver with an upper and lower limit. ")
a = int(input("constant = "))
b = input("variable = ")
c = float(input("power = "))

d = c + 1

print("The formula is " + str(a*c) + str(b) + "^" + str(d-1))

power = int(d)
upper = int(input("upper limit = "))
lower = int(input("lower limit = "))

sol1a = upper**power
sol2a = lower**power

print(str(sol1a) + str(sol2a))

sol1b = sol1a * a
sol2b = sol2a * a

print(str(sol1b) + str(sol2b))
sol1c = sol1b / d
sol2c = sol2b / d
print(str(sol1c) + str(sol2c))

final = sol1c - sol2c
ans = str(final)

print(ans)
print(b + " = " + ans )