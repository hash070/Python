n = int(input())
# 首先对输入的第二行分割成一个列表
# 然后使用map(func,[list])方法对列表中的每一个字符串强转为int
# 最后再将map返回的迭代器用list转换成数字列表
arr = list(map(int, input().split()))
# 直接使用sorted进行分类
arr = sorted(arr)
# join方法用于将序列中的元素以指定字符连接，生成一个新的字符串
# 例如print("-".join(("1","2","3"))) ==> 1-2-3
output_str = ' '.join(map(str, arr))
print(output_str)