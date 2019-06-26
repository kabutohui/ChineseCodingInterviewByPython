# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入n个正整数，找出其中最小的k个数，如输入4， 5， 1， 6， 2， 7， 3， 8这8个数字，最小的4个数字是1，2，3，4。

【解题思路】：

可以先排序，然后再取前k个数字，时间复杂度：O（nlogn）;
利用快排的思想找到第k大的数字，然后k右边的数字就是最小的k个数，这个方法的平均复杂度为O(n)；
建立大小为k的辅助空间，依次从n中读入数据，用小的数据替换k中的最大的数据，遍历完成之后，k中就是最小的k个数。
'''


# method 1: use partition
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


def getLeastNumbers_Partition(nums, k):
    if not nums or k <= 0:
        return
    start, end = 0, len(nums) - 1
    index = partition(nums, start, end)

    while index != k:
        if index > k - 1:
            index = partition(nums, start, index - 1)
        else:
            index = partition(nums, index - 1, end)

    return nums[:k]


# --------------------------------------------------------

def max_heapify(A, i, len):
    '''
    维护最大堆
    '''
    l = 2 * i + 1
    r = 2 * i + 2

    if l < len and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < len and A[r] > A[largest]:
        largest = r

    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        max_heapify(A, largest, len)
    return A


def build_max_heapify(A):
    '''
    构建最大堆
    '''
    for i in range(len(A) // 2 - 1, -1, -1):
        max_heapify(A, i, len(A))


# method 2: use extra space
def getLeastNumbers_AssistSpace(nums, k):
    if not nums or k <= 0:
        return
    k_help, count = [], 0
    for i in nums:
        if count < k:
            k_help.append(i)
            # 构建最大堆
            build_max_heapify(k_help)
            count += 1
        else:
            # 比较k_help中的最大值和i
            k_help[0] = min(k_help[0], i)
            # 维护最大堆
            max_heapify(k_help, 0, k)

    return k_help


# test
nums = [4, 5, 1, 6, 2, 7, 3, 8]
print("Method 1: use partition:", getLeastNumbers_Partition(nums, 4))
print("Method 2: use extra space:", getLeastNumbers_AssistSpace(nums, 4))