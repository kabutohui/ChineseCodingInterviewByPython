# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个字符串，将这个字符串转化为整数。

【解题思路】：
问题不难，但是需要考虑到的边界条件很多：

输入是否合法？
输出是否越界？
结果是否移除？
'''


def strToInt(string):
    if not string:
        return "The string is empty"

    minus = False
    num = 0

    for i, s in enumerate(string):
        if i == 0:
            if s == "-":
                minus = True
            elif s == "+":
                minus = False
            elif s.isdigit():
                num = int(s)
            else:
                return "illegal input!"
        else:
            if s.isdigit():
                num = num * 10 + int(s)
            else:
                return "illegal input!"

    return max(-num, -2 ** 31) if minus else min(num, 2 ** 31 - 1)


# test
strToInt("-1231123")