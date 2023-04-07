"""
n = int(input())
sum = 1
for i in range(1,n+1):
    sum *= i
print(sum)
"""

n = int(input())

# 定义数组
a = [1]

# 从1~n迭代，每次都将a乘以当前的数i，注意进位
for i in range(1, n+1):
    c = 0
    for j in range(len(a)):
        t = a[j] * i + c
        a[j] = t % 10
        c = t // 10
    while c:
        a.append(c % 10)
        c //= 10

# 倒序输出数组中的元素，即为阶乘的结果
print(''.join(map(str, a[::-1])))