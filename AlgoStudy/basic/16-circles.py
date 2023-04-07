import math

r = float(input())

pi = math.pi

x = pi * r * r

x = round(x, 7)

x_len = len(str(x).split('.')[1])

print(str(x)+"0"*(7-x_len))