import string
# n ,m = map(int,input().split())
# origin_str = string.ascii_uppercase[:m]

# for i in range(1,n+1):
#     print(str(origin_str[0:i][::-1]+origin_str[1:])[:m])
n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        print(string.ascii_uppercase[abs(i-j)],end='')
    print()