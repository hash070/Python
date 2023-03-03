n = int(input())
# init triangler
res = [[1]*(i+1) for i in range(n)]
# print(res)
for row in range(2, n):
    for col in range(1, row):
        res[row][col] = res[row-1][col-1] + res[row-1][col]

print(res)
for i in range(n):
    print(' '.join(str(num) for num in res[i]))
