n = int(input())

# 枚举五位数和六位数
for num in range(10000, 1000000):
    digits_sum = sum(int(digit) for digit in str(num))  # 计算数字的各位数字之和
    if digits_sum == n:  # 如果数字的各位数字之和等于n
        if str(num) == str(num)[::-1]:  # 如果数字是回文数
            print(num)
