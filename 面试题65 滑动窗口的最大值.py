# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
给定一个数组和滑动窗口的大小，找出所有滑动窗口里的最大值。
如{2，3，4，2，6，2，5，1}和窗口大小3，那么一共有6个滑动窗口，每个滑动窗口的最大值为{4，4，6，6，6，5}。

【解题思路】：
利用队列的思想，将当前最大的数和可能最大数存起来，根据当前数与最大数的下标来判断最大的数是否已经滑出窗口。
'''


def maxInWindows(nums, windowSize):
    if not nums or windowSize <= 0:
        return []
    if windowSize >= len(nums):
        return [max(nums)]

    queue, res = [], []

    # the first window
    for i in range(windowSize):
        while queue and nums[i] >= nums[queue[-1]]:
            queue.pop(-1)
        queue.append(i)

    # for the rest of the windows
    for i in range(windowSize, len(nums)):
        res.append(nums[queue[0]])

        while queue and nums[i] >= nums[queue[-1]]:
            queue.pop(-1)
        if queue and queue[0] <= (i - windowSize):
            queue.pop(0)

        queue.append(i)

    res.append(nums[queue[0]])

    return res


# test
nums = [2, 3, 4, 2, 6, 2, 5, 1]
res = maxInWindows(nums, 3)
print(res)