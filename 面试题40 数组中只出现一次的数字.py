# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
一个整数数组中，除了两个数字外，其他的数字都出现了2次。请编程找出只出现一次的数字。
要求： 时间复杂度： O(n) ，空间复杂度： O(1) 

【解题思路】：
可以使用异或，因为最多数字出现2次，那么重复的数字在异或运算中就会消失。
对于数组中只有一个只出现一次的数：直接异或每一个数字，最终的结果就是只出现一次的数；
如果数组中有两个只出现一次的数：将数组分成两个部分，即每个部分都只包含一个重复的数。其方法为：

先将所有数进行异或，找到最终异或运算结果的二进制中第一个1出现的位置，记作第n位；
根据第n位置是不是1，将数组分成两组，最后将这两个子数组进行异或运算，就能得到只出现一次的两个数。
'''


def findNumsAppearOnce(nums):
    if not nums:
        return
    OR_result = 0
    for i in nums:
        OR_result ^= i

    indexOf1 = findFirstBitOf1(OR_result)

    num1, num2 = 0, 0

    for i in nums:
        if isBit1(i, indexOf1):
            num1 ^= i
        else:
            num2 ^= i

    return num1, num2


def findFirstBitOf1(OR_result):
    indexBit = 0
    while OR_result & 1 == 0:
        OR_result = OR_result >> 1
        indexBit += 1
    return indexBit


def isBit1(num, indexOf1):
    num = num >> indexOf1
    return num & 1


# test
nums = [2, 4, 3, 6, 3, 2, 5, 5]
findNumsAppearOnce(nums)