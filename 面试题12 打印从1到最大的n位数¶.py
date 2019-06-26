# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入数字n，按顺序打印从1到最大的n位十进制数。比如输入3，则打印1，2，3，...，999。

【解体思路】：

这个题目需要考虑大数的问题，使用字符串来表示这个数字，然后在字符串上模拟加法。
还可以使用递归方法，将问题转化成数字的全排列。
'''


# Iterative method
def printDigits_Iterative(n: int):
    if n <= 0:
        return
    number = [0] * n
    while True:
        isOverFlow = False
        carry = 0
        for i in range(len(number) - 1, -1, -1):
            if i == len(number) - 1:
                isum = number[i] + 1
                if isum == 10:
                    if i == 0:
                        return
                    carry = 1
                    number[i] = 0
                else:
                    carry = 0
                    number[i] = isum
            else:
                if carry == 1:
                    isum = number[i] + carry
                    if isum == 10:
                        if i == 0:
                            return
                        carry = 1
                        number[i] = 0
                    else:
                        carry = 0
                        number[i] = isum
                else:
                    break

        printNumber(number)


def printNumber(number):
    for i in range(len(number)):
        if number[i] != 0:
            break
    if i == len(number) - 1 and number[i] == 0:
        return
    res = "".join(str(j) for j in number[i:])
    print(res, end=" ")


printDigits_Iterative(2)


# -----------------------------------------------
# Recursive method
def printDigits_Recursive(n: int):
    if n <= 0:
        return
    number = [0] * n

    def recursive(number, index):
        if index == len(number):
            printNumber(number)
            return
        for i in range(10):
            number[index] = i
            recursive(number, index + 1)

    recursive(number, 0)


printDigits_Recursive(2)