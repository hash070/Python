n = int(input())

# 生成杨辉三角
triangle = [[1] * (i+1) for i in range(n)]
# print(triangle)
for i in range(2, n):
    for j in range(1, i):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

# 输出杨辉三角
for i in range(n):
    print(' '.join(str(num) for num in triangle[i]))