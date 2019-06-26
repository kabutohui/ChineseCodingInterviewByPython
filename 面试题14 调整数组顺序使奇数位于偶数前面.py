# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个整数数组，实现一个函数来调整数组中数字的顺序，使得所有的奇数位于数组前半部分，偶数位于数组后半部分。

【解题思路】：
使用双指针，一个从前往后搜索【指向偶数】，一个从后往前搜索【指向奇数】。直到来给你个指针重合。
'''


def reorderOddEven(nums: list) -> list:
    if len(nums) == 0:
        return
    first, second = 0, len(nums) - 1

    while first < second:
        while first < len(nums) and nums[first] & 1 == 0:
            first += 1
        while second > 0 and nums[second] & 1 == 1:
            second -= 1

        if first < second:
            temp = nums[first]
            nums[first] = nums[second]
            nums[second] = temp

    return nums


# test
reorderOddEven([2, 1, 3, 5, 4, 6])