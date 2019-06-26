# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。  
如9的二进制为：1001，输出结果为2。  

【解题思路】：  
1. 利用位移的思想，每次先与1进行与运算，再将该数右移一位；  
2. 先将该数字对2求余，再除以2，直到结果为0。  

**Note:**位运算比除法效率要高
'''


def numberOf1(n: int) -> int:
    count = 0
    while n:
        if n & 1:
            count += 1
        n = n >> 1
    return count


def numberOf1_2(n: int) -> int:
    count = 0
    while n:
        if n % 2 != 0:
            count += 1
        n = n // 2

    return count


# 这个方法非常巧妙，且效率很高，因为数字中有多少个1就会进行几次循环
def numberOf1_3(n: int) -> int:
    count = 0
    while n:
        count += 1
        n = (n - 1) & n

    return count


# test
n = 9
print("numberOf1: ", numberOf1(n))
print("numberOf1_2: ", numberOf1_2(n))
print("numberOf1_3: ", numberOf1_3(n))