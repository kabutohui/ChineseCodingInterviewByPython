# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个整型数组，数组里有正数也有负数。数组中一个或连续多个整数组成一个子数组，求所有子数组和的最大值。要求时间复杂度为O(n)。
如{1， -2， 3， 10， -4， 7， 2， -5}和最大的子数组为{3， 10， -4， 7， 2}。

【解题思路】：

分析数组的规律：
从头到尾累加，如果发现累加的和小于0，则丢弃之前的数据，从新的数据开始累加；
如果加入新的数据后，和下降，则保留原来最大的和。
利用动态规划：
用函数f(i)表示以第i个数字结尾的字数组的最大和，最后只需要求出max(f(i))，可以利用如下的递推公式：
f(n)={Data[i],i=0 or f(i−1)<0f(i−1)+Data[i],i≠0 and f(i−1)>0
'''


# method 1
def findGreatestSumOfSubArray(nums):
    if not nums:
        return

    greatestSum, curSum = -2 ** 31, 0
    for val in nums:
        if curSum < 0:
            curSum = val
        else:
            curSum += val

        if curSum > greatestSum:
            greatestSum = curSum

    return greatestSum


# method 2: use DP
def findGreatestSumOfSubArray_DP(nums):
    if not nums:
        return

    f = [0] * len(nums)
    for i, val in enumerate(nums):
        if i == 0 or f[i - 1] <= 0:
            f[i] = val
        else:
            f[i] = f[i - 1] + val

    return max(f)


# test
# nums = [1, -2, 3, 10, -4, 7, 2, -5]
nums = [-1, -2, -3, -4, -5]
print("Method 1:", findGreatestSumOfSubArray(nums))
print("Method 2:", findGreatestSumOfSubArray_DP(nums))