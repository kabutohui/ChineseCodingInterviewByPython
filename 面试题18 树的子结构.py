# -*- coding: utf-8 -*-

'''
@Author:    kabuto
@Date:      2019/06/26
'''

'''
【题目】：
输入两颗二叉树A和B，判断B是不是A的子结构。

【解题思路】：
还是利用递归的思想：

先找到A中与B的根节点相同的节点；
再判断其结构是否一样；
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
def hasSubTree(root1, root2):
    result = False
    if root1 and root2:
        if root1.val == root2.val:  # has the same root value
            result = doseTree1HasTree2(root1, root2)
        if not result:
            result = hasSubTree(root1.left, root2)
        if not result:
            result = hasSubTree(root1.right, root2)

    return result


def doseTree1HasTree2(root1, root2):
    if not root2:
        return True
    if not root1:
        return False
    if root1.val != root2.val:
        return False

    return doseTree1HasTree2(root1.left, root2.left) and doseTree1HasTree2(root1.right, root2.right)


root1 = createTree([8, 8, 7, 9, 2, None, None, None, None, 4, 7], 0)
root2 = createTree([8, 9, 2], 0)
hasSubTree(root1, root2)