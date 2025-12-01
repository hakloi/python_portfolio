import math

# a = int(input("Input a: "))
# b = int(input("Input b: "))
# c = int(input("Input c: "))

a = 7
b = 5
c = 3

dis = b** 2- 4*a*c
x1 = (-b +math.sqrt(dis))/(2*a)
x2 = (-b -math.sqrt(dis))/(2*a)

print(x1, x2)