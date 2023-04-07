for i in range(32):
    binary_str = format(i, '05b')  # 将整数转换为长度为 5 的二进制字符串，用 0 补充不足的位数
    print(binary_str)