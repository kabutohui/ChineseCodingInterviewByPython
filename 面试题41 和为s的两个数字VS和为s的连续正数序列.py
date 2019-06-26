# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目一】：
输入一个递增排序的数组和一个数s，在数组中查找两个数，使得他们的和正好是s。如果有多对数字的和为s，输出任意一对即可。

【题目二】： 输入一个正整数s，打印出所有和为s的连续正数序列（至少包含两个数）。如输入15，则1+2+3+4+5=4+5+6=7+8=15，所以输出3个连续序列1-5，4-6，7-8。

【解题思路】：
题目一： 利用双指针的思想解题即可；
题目二： 还是利用双指针，先递增右指针（指向较大的数），直到和等于target，如果大于target，则递增左指针（指向较小的数），直到满足要求或者左指针指向 1+target2
'''


# Question 1
def findNumbersWithSum(nums, target):
    if not nums:
        return
    start, end = 0, len(nums) - 1

    while start < end:
        if nums[start] + nums[end] == target:
            return [nums[start], nums[end]]
        elif nums[start] + nums[end] > target:
            end -= 1
        else:
            start += 1

    return "No such two numbers!"


# Quesetion 2
def findContinuousSequence(target):
    if target < 3:
        return
    small, big = 1, 2
    mid = (1 + target) // 2
    curSum = small + big

    while small < mid:
        if curSum == target:
            print([i for i in range(small, big + 1)])
            big += 1
            curSum += big
        elif curSum > target:
            curSum -= small
            small += 1
        else:
            big += 1
            curSum += big


# test
nums = [1, 2, 4, 7, 11, 15]
findNumbersWithSum(nums, 15)
findContinuousSequence(100)