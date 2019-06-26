# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
我们把只包含因子2，3和5的数称为丑数（Ugly Number）。求按从小到大的顺序的第1500个丑数。例如6，8是丑数，但是14不是。习惯上我们把1当作第一个丑数。

【解题思路】：
思路一： 写一个丑数的判断程序，然后遍历到指定个数的丑数即可【效率低】；
思路二：记录最新的2， 3， 5的倍数，然后选取最小的作为新的丑数，这样可以使丑数的生成是按照顺序的。
'''


# Method 1,
def isUglyNumber(num):
    if num < 1:
        return "Error"
    while num % 2 == 0:
        num = num / 2
    while num % 3 == 0:
        num = num / 3
    while num % 5 == 0:
        num = num / 5

    return True if num == 1 else False


def getUglyNumber(index):
    if index < 1:
        return "Error"
    count, num = 0, 0
    while count < index:
        num += 1
        if isUglyNumber(num):
            count += 1

    return num


# Method 2
def getUglyNumber2(index):
    if index < 0:
        return
    currentUgly, multiply2, multiply3, multiply5 = [0] * index, 0, 0, 0
    currentUgly[0] = 1
    count = 1

    while count < index:
        currentUgly[count] = min(currentUgly[multiply2] * 2, currentUgly[multiply3] * 3, currentUgly[multiply5] * 5)

        while currentUgly[multiply2] * 2 <= currentUgly[count]:
            multiply2 += 1
        while currentUgly[multiply3] * 3 <= currentUgly[count]:
            multiply3 += 1
        while currentUgly[multiply5] * 5 <= currentUgly[count]:
            multiply5 += 1

        count += 1

    return currentUgly[-1]


# test
getUglyNumber2(1500)  # more efficient
# getUglyNumber2(1500) # slowly 859963392