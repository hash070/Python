n = int(input())

# initilize
f1, f2 = 1, 1

for i in range(3, n+1):
    # 计算第 i 项目
    fn = f1 + f2

    # 更新前两项 但是不直接计算准确数值 防止过大的内存占用或溢出
    f1, f2 = f2, fn % 10007

print(f2 % 10007)
