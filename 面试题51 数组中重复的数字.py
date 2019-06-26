# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
在一个长度为n的数组中，所有数字都在0-n-1的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。如{2, 3, 1, 0, 2, 5, 3}，那么对应输出的重复数字是2，或者3。

【解题思路】：
思路一：
利用dict，判断数字是否已经出现过，已经出现过的数字为重复数据，直接返回。【需要额外的内存】

思路二：

以此扫描这个数组，判断当前数字m与下标index是否相等，不相等则与下标为m的数字进行交换；
直到发现一个重复的数字；【时间复杂度： O(n) ， 空间复杂度： O(1) 】
'''


# Method 1
def findDuplicate_extraMemory(nums):
    if not nums:
        return

    record = {}

    for i in nums:
        if i not in record.keys():
            record[i] = 0
        else:
            return i

    return "No such number!"


# Method 2
def findDuplicate_OneExtraMemory(nums):
    if not nums:
        return

        # check the numbers of the array
    for i in nums:
        if i < 0 or i > len(nums) - 1:
            return "Illegal input, the number must between 0 and len(nums)-1!"

    # find the first duplicate number
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            temp = nums[i]
            nums[i] = nums[temp]
            nums[temp] = temp

    return "No such number!"


# test
nums = [2, 3, 1, 0, 2, 5, 3]
print("Mehtod 1:", findDuplicate_extraMemory(nums))
print("Method 2:", findDuplicate_OneExtraMemory(nums))