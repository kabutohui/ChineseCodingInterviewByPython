# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
从扑克牌中随机抽取5张牌，判断是不是个顺子，即这5张牌是不是连续的。2-10为数字本身，A为1，J为11，Q为12，K为13，大小王为任意数字。

【解题思路】：
先将扑克牌除去大小王外定义成2-13的数字，然后大小王设置为0，将数组排序后，用0去填补空缺。主要步骤有：

先将数组排序；
统计0和空缺的个数，如果0的个数大于等于空缺的个数，就为顺子，否则不是；
如果出现对子，那么一定不是连续的。
'''


def isContinuous(nums):
    if not nums:
        return False

    nums.sort()
    numOfZero, numOfGap = 0, 0

    # count the number of the zero
    for i in nums:
        if i == 0:
            numOfZero += 1

    # count the number of gap
    small = numOfZero
    big = small + 1
    while big < len(nums):
        # if the nums have the same value,return false
        if nums[small] == nums[big]:
            return False
        numOfGap += nums[big] - nums[small] - 1
        small = big
        big += 1

    return True if numOfZero >= numOfGap else False


# test
nums1 = [2, 3, 4, 1, 6]
nums2 = [0, 0, 4, 7, 9]
nums3 = [0, 4, 3, 5, 1]
nums4 = [0, 0, 1, 1, 2]

print("test1:", isContinuous(nums1))
print("test2:", isContinuous(nums2))
print("test3:", isContinuous(nums3))
print("test4:", isContinuous(nums4))
