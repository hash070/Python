"""
【问题描述】

小蓝有很多数字卡片,每张卡片上都是数字0到9。

小蓝准备用这些卡片来拼一些数,他想从1开始拼出正整数,每拼一个,就保存起来,卡片就不能用来拼其它数了。

小蓝想知道自己能从1拼到多少。

例如,当小蓝有30张卡片,其中0到9各3张,则小蓝可以拼出1到10,但是拼11时卡片1已经只有一张了,不够拼出11。

现在小蓝手里有0到9的卡片各2021张,共20210张,请问小蓝可以从1拼到多少?

提示：建议使用计算机编程解决问题。【答案提交】

这是一道结果填空的题,你只需要算出结果后提交即可。本题的结果为一个整数,在提交答案时只填写这个整数,填写多余的内容将无法得分。
"""

"""


# 0 - 9 => 10
total = [2021]*10

i = 1

flag = False

while not flag:
    temp_list = list(str(i))
    for temp_str in temp_list:
        temp_int = int(temp_str)
        if total[temp_int] == 0:
            print(i-1)
            flag = True
            break
        total[temp_int] -= 1
    i += 1

#---
    
total = [2021] * 10

i = 1
flag = False

while not flag:
    temp_list = list(str(i))
    
    # 检查是否有足够的卡片来拼出当前数字
    enough_cards = True
    for temp_str in temp_list:
        temp_int = int(temp_str)
        if total[temp_int] == 0:
            enough_cards = False
            break
            
    # 如果没有足够的卡片，输出上一个数字（i - 1），并跳出循环
    if not enough_cards:
        print(i - 1)
        flag = True
    else:
        # 如果有足够的卡片，从 total 中减去相应的卡片数量，并检查下一个数字
        for temp_str in temp_list:
            temp_int = int(temp_str)
            total[temp_int] -= 1
        i += 1
"""


"""

# 直线


"""