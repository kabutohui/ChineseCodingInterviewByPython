# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果，是返回True，不是返回False。
假设输入的数组任意两个数字都互不相同

【解题思路】：
在后序遍历中，最后一个数字就是树的根节点的值。而数组前面的部分可以分成两个部分：

第一部分是左子树节点的值，他们都比根节点的值小；
第二部分是右子树节点的值，他们都比根节点的值大。
'''


def verifySquenceOfBST(nums: list) -> bool:
    if not nums:
        return False

    if len(nums) == 1:
        return True

    root = nums[-1]
    i, j = 0, 0
    # find the value in nums less than the root
    for i in range(len(nums) - 1):
        if nums[i] > root:
            break

    # find the value in nums gather than the root
    for j in range(i, len(nums) - 1):
        if nums[j] < root:
            return False

    # is left subtree a BST?
    left = True
    if i > 0:
        left = verifySquenceOfBST(nums[:i])

    # is right subtree a BST?
    right = True
    if i < len(nums) - 1:
        right = verifySquenceOfBST(nums[i:len(nums) - 1])

    return left and right


verifySquenceOfBST([5, 7, 6, 9, 11, 10, 8])