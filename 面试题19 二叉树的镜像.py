# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
完成一个函数，输入一个二叉树，该函数输出它的镜像。

【解题思路】：
还是使用递归的思想：

先交换左右子树；
再对子树中的子树进行交换。
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


# print tree
def preOrder(root):
    if not root:
        return
    print(root.val, end=" ")
    preOrder(root.left)
    preOrder(root.right)


# Solution
def mirrorRecursively(root):
    if not root:
        return
    if not root.right and not root.left:  # if node is the leaf
        return
    temp = root.left
    root.left = root.right
    root.right = temp

    mirrorRecursively(root.left)
    mirrorRecursively(root.right)


# test
root = createTree([8, 6, 10, 5, None, None, 11], 0)
pNode = root
print("Before:")
preOrder(root)
mirrorRecursively(pNode)
print("\nAfter:")
preOrder(root)