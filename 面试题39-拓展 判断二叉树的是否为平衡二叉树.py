# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一个二叉树，判断这个二叉树是不是平衡二叉树。平衡二叉树是指任意节点左右子树高度之差不超过1。

【解题思路】：
在遍历的过程中，判断每个节点是不是平衡二叉树，返回高度和判断信息。
'''


class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def isBalance(root, depth):
    if not root:
        return (True, 0)

    left = isBalance(root.left, depth)
    right = isBalance(root.right, depth)

    return (left[0] & right[0] & (abs(left[1] - right[1]) > 1), max(left[1], right[1]) + 1)


# test
# create a tree
def createTree(nums, index):
    if not nums:
        return None
    if index >= len(nums):
        return None

    root = TreeNode(nums[index])
    root.left = createTree(nums, 2 * index + 1)
    root.right = createTree(nums, 2 * index + 2)

    return root


root = createTree([1, 2, 3, None, 5, None, 6, None, None, 7], 0)
res = isBalance(root, 0)
print("Depth =", res[1], "isBalance =", res[0])