# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一颗二叉树的根节点，求该二叉树的深度。二叉树的深度是从根节点到叶子节点所形成的最长的路径。

【解题思路】：
典型的递归的题目，分别求取左子树和右子数的深度，然后将最大的值加1进行返回。
'''

class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def treeDepth(root):
    if not root:
        return 0

    left = treeDepth(root.left)
    right = treeDepth(root.right)

    return max(left, right) + 1


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
res = True
treeDepth(root)
