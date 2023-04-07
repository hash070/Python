# a, b = [int(i) for i in input().split()]

a, b = [[int(j) for j in list(i)] for i in input().strip().split()]
c = [0] * (len(a) + 1)

carry = 0  # 进位

if len(a) < len(b):
    a, b = b, a
n = len(a)
m = len(b)
for i in range(len(a)):
    if i < m:
        s = a[n - 1 - i] + b[m - 1 - i] + carry
    else:
        s = a[n - 1 - i] + carry

    carry = s // 10  # 计算进位
    c[n - i] = s % 10  # 计算当前位的结果

# 处理最高位的进位
if carry == 1:
    c[0] = 1
else:
    c = c[1:]

print(''.join(map(str, c)))
