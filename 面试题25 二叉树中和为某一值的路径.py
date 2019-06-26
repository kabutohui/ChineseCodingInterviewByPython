# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入一颗二叉树和一个整数，打印出二叉树中节点值和为输入整数的所有路径。
规定： 从树的根节点开始往下一直到叶节点所经过的节点形成一条路径

【解题思路】：
这道题可以利用前序遍历来做，纪录从根节点到叶子节点的所有值，如果路径上节点的和等于输入整数，就存下来。
'''


# define the tree
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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


def findPath(root, expected):
    if not root:
        return

    res = []

    def recursive(root, expected, temp):
        temp.append(root.val)
        if root.left == None and root.right == None:
            if sum(temp) == expected:
                print(temp)

        if root.left != None:
            recursive(root.left, expected, temp)
        if root.right != None:
            recursive(root.right, expected, temp)
        # delete current treeNode before return to the parent node
        temp.pop(-1)

    recursive(root, expected, [])


# test
# 1. create tree
root = createTree([10, 5, 12, 4, 7], 0)
# 2. find path
findPath(root, 22)