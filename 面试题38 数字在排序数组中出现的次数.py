# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
统计一个数字在排序数组中出现的次数。例如输入一个排序数组{1， 2， 3， 3， 3， 3， 4， 5}和数字3，输出结果为4。

【解题思路】：
分别使用二分法找到第一个和最后一个目标数的位置。
'''


def findFirstK(nums, k, start, end):
    if not nums:
        return
    if start > end:
        return -1

    mid = (start + end) // 2

    if nums[mid] == k:
        if mid > 0 and nums[mid - 1] != k or mid == 0:
            return mid
        else:
            end = mid - 1
    elif nums[mid] > k:
        end = mid - 1
    else:
        start = mid + 1

    return findFirstK(nums, k, start, end)


def findLastK(nums, k, start, end):
    if not nums:
        return
    if start > end:
        return -1

    mid = (start + end) // 2

    if nums[mid] == k:
        if mid < len(nums) - 1 and nums[mid + 1] != k or mid == len(nums) - 1:
            return mid
        else:
            start = mid + 1
    elif nums[mid] > k:
        end = mid - 1
    else:
        start = mid + 1

    return findLastK(nums, k, start, end)


def getNumberOfK(nums, k):
    if not nums:
        return

    first = findFirstK(nums, k, 0, len(nums) - 1)
    last = findLastK(nums, k, 0, len(nums) - 1)

    if first != -1 and last != -1:
        return last - first + 1
    else:
        return 0


# test
nums = [1, 2, 3, 3, 3, 3, 4, 5, 6]
getNumberOfK(nums, 3)