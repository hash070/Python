n = int(input())
for i in range(n):
    hex_str = input()
    # 16进制转换为10进制
    decimal_int = int(hex_str, 16)
    # octonary number system 八进制
    # oct转成八进制，然后，切去前导0o
    octal_str = oct(decimal_int)[2:]
    print(octal_str)
