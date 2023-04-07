# A sort the string alphabet

# a = "EACG"

# a_list = list(a)

# mylist = ["b", "C", "A"]

# b = [i.upper() for i in mylist]


# print(sorted(mylist))

# c = "WHERETHEREISAWILLTHEREISAWAY"

# print(''.join(sorted(c)))


# B find int

# for i in range(10**17):
#     a = i % 2 == 1
#     b = i % 3 == 2
#     c = i % 4 == 1
#     d = i % 5 == 4
#     if a and b and c and d :
#         print(i)
#         break

# C ax paper

import sys

type = list(input())

type_index = int(type[1])

print(type_index)

x, y = 1189, 841

# if type_index == 0:
#     print(f'{x} {y}')
#     sys.exit()

for i in range(type_index+1):
    if i == 0:
        continue
    if x > y:
        x //= 2
    else:
        y //= 2

if x < y:
    x,y=y,x

print(f"{x} {y}")

