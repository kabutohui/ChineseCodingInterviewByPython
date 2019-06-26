# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
如{1，2，3，2，2，2，5，4，2}， 2在数组中出现了5次，因此输出2。

【解题思路】：
一、基于Partition的O(n)解法：

数组中有数字出现的次数超过数组长度的一半，那么将其排序，【中位数】就是我们要找的数字；
利用O(n)的算法找数组中任意第k大的数字。
a). 任意选择一个数字，将比他大的放在左边，比他小的放在右边；
b). 如果这个选中的数字下标为n/2，那么他就是中位数；
c). 如果大于n/2，则中位数在其左边，否则在其右边。
二、基于数组的特点：
在遍历数组的时候保存两个值：一个是数组中的一个数字；一个是次数。

当我们遍历到下一个数字的时候，如果与我们之前保存的数字相同，则次数+1；
如果下一个数字与上一个数字不同时，次数-1；
如果次数为0，我们需要保存下一个数字，并将次数设置为1；
由于我们要找的数字比其他所有数字出现次数之和还要多，所以我们要找的数字就是最后一次将次数设置为1的那个数字
'''


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            temp = A[j]
            A[j] = A[i]
            A[i] = temp
    temp = A[r]
    A[r] = A[i + 1]
    A[i + 1] = temp
    return i + 1


def quicksort(A, p, r):
    if p < r:
        print('before:', A, end="")
        q = partition(A, p, r)
        print('after:', q, A)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


# method 1: use partition
def moreThanHalfNum1(nums):
    middle = len(nums) // 2
    start, end = 0, len(nums) - 1
    index = partition(nums, start, end)
    while index != middle:
        if index > middle:
            index = partition(nums, start, index - 1)
        else:
            index = partition(nums, index + 1, end)

    result = nums[middle]

    count = 0
    for i in nums:
        if i == result:
            count += 1
        if count > middle:
            return result

    return "No such number!"


# method 2: use the character of the array
def moreThanHalfNum2(nums):
    if not nums:
        return
    result, times = nums[0], 1
    for i in range(1, len(nums)):
        if times == 0:
            result = nums[i]
            times = 1
        elif nums[i] == result:
            times += 1
        else:
            times -= 1

    count = 0
    for i in nums:
        if i == result:
            count += 1
        if count > len(nums) >> 1:
            return result

    return "No such number!"


moreThanHalfNum2([1, 2, 3, 3, 2, 2, 2, 5, 2])