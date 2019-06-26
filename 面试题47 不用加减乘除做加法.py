# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
写一个函数，求两个整数之和，要求在函数体内不能使用四则运算符号。

【解题思路】：
如果不能使用四则运算，则需要采用位运算来实现加法：

先将两个数做异或运算；
再将两个数进行与运算，并左移一位形成进位，直到不产生进位为止。
'''


def Add(num1, num2):
    sum, carry = 0, 0
    while num2 != 0:
        sum = num1 ^ num2
        carry = (num1 & num2) << 1

        num1 = sum
        num2 = carry

    return num1


# test
Add(0, -9)