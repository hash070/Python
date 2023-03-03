# n = int(input())

# arr = list(map(int, input().split()))

# tar = int(input())
# # if founded
# flag = True

# for i in range(n):
#     if (tar == arr[i]):
#         print(i+1)
#         # flag it and break
#         flag = False
#         break

# # if not founded
# if (flag):
#     print(-1)

n = int(input())
nums = list(map(int, input().split()))
target = int(input())

for i in range(n):
    if nums[i] == target:
        print(i + 1)
        break
else:
    print(-1)

