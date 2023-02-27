# 问题描述
# 　　153是一个非常特殊的数，它等于它的每位数字的立方和，即153=1*1*1+5*5*5+3*3*3。编程求所有满足这种条件的三位十进制数。
# 输出格式
# 　　按从小到大的顺序输出满足条件的三位十进制数，每个数占一行。

for i in range(100,1000):
    j = [int(d) for d in str(i)]
    sum_of_cubes = sum(k**3 for k in j)
    if sum_of_cubes == i:
        print(i)


# 枚举所有三位数
for num in range(100, 1000):
    # 将数字转换为字符串，并拆分各个位上的数字
    digits = [int(d) for d in str(num)]
    # 计算数字的各位数字的立方和
    sum_of_cubes = sum(digit**3 for digit in digits)
    if num == sum_of_cubes:  # 如果数字满足条件
        print(num)  # 输出这个数

# print("153\n370\n371\n407")