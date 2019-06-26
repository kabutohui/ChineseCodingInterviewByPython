# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
把一个数组最开始的若干元素搬到数组的末尾，我们称之为数组的旋转。输入一个【递增】排序的数组的一个旋转，输出旋转数组的最小元素。
如{3， 4， 5， 1， 2}是{1， 2， 3， 4， 5}的一个旋转，最小元素是1。

【解题思路】：
设置前后指针，通过更新指针，直到两个位置只差为1的时候，第二个指针所指向的位置就是最小元素。

需要注意的是两个指针指向的位置的元素一样时，就需要遍历了，如{1， 1， 1， 0， 1}
'''


def Min(nums: list) -> int:
    if not nums:
        return "None"
    index1, index2 = 0, len(nums) - 1
    indexMid = index1

    while nums[index1] >= nums[index2]:
        if index2 - index2 == 1:
            return nums[index2]

        indexMid = (index1 + index2) // 2
        # 如果index1， index2， indexMid指向的元素相同的话，需要进行遍历
        if nums[index1] == nums[index2] and nums[index1] == nums[indexMid]:
            minNum = nums[index1]
            for i in nums[index1 + 1: index2 + 1]:
                minNum = min(minNum, i)

            return minNum

        if nums[index1] >= nums[index2]:
            index1 = indexMid
        elif nums[index1] <= nums[index2]:
            index2 = indexMid

    return nums[indexMid]


# test
nums = [3, 4, 5, 1, 2]
print("[3,4,5,1,2]:", Min(nums))
nums = [1, 1, 1, 0, 1]
print("[1,1,1,0,1]:", Min(nums))